import requests
import httpx
import asyncio
from django.conf import settings
from core.models import Author
from celery import shared_task

@shared_task
def create_or_update_authors_lazy(authors_data):
    create_or_update_authors(authors_data)

@shared_task
async def sync_author_from_api_lazy(author_ids, author_details_api_url):
    asyncio.run(sync_author_from_api_lazy(author_ids, author_details_api_url))

async def sync_author_from_api(author_ids, author_details_api_url):
    # Fetch content list from the first third-party API
    async with httpx.AsyncClient() as client:

        # Fetch author details asynchronously for each content
        author_details_tasks = [
            get_author_details(
                client, author_id, author_details_api_url, get_request_headers()
            )
            for author_id in author_ids
        ]
        author_details = await asyncio.gather(*author_details_tasks)
    # Call celery task for syncing data
    create_or_update_authors_lazy.delay(author_details)

def get_dict_by_field_value(lst, field, value):
    for item in lst:
        if item.get(field) == value:
            return item
    return {}

def create_or_update_authors(authors_data):
    seen_ids = set()
    # Define a lambda function to create a unique identifier for each dictionary
    identifier = lambda item: (item.get('unique_id', ''))
    # Use a list comprehension to filter out duplicates
    unique_data = [item for item in authors_data if (_id := identifier(item)) not in seen_ids and not seen_ids.add(_id)]
    authors_data = unique_data
    authors_data = [item for item in authors_data if item]
    unique_ids = []
    unique_ids = list(set(map(lambda item: item.get('unique_id', ''), authors_data)))
    unique_ids = [item for item in unique_ids if item]
    author_unique_id_from_db = list(Author.objects.filter(
        unique_id__in=unique_ids
    ).values_list('unique_id', flat=True))
    author_to_be_created = []
    author_to_be_updated = []
    for author in authors_data:
        author_unique_id = author.get('unique_id')
        if author_unique_id in author_unique_id_from_db:
            data_from_db = Author.objects.get(unique_id=author_unique_id)
            data_from_db.data = author
            author_to_be_updated.append(data_from_db)
        else:
            author_to_be_created.append(
                Author(
                    unique_id=author_unique_id,
                    data=author
                )
            )
    # Create new authors
    Author.objects.bulk_create(author_to_be_created)
    # Update existing authors
    Author.objects.bulk_update(author_to_be_updated, ['data'])


def generate_full_api_url(api_url_path):
    """Generate a full api url from a api path

    Args:
        api_url_path (string): api path of an api

    Returns:
        string: the full api url path for an api
    """
    base_api_url = settings.ZELF_HACK_API_BASE_URL
    return f"{base_api_url}/{api_url_path}"


def get_request_headers():
    """prepare request headers zelf hack api

    Returns:
        dict: request headers object
    """
    api_key = settings.ZELF_HACK_API_KEY
    headers = {"x-api-key": api_key}
    return headers

async def get_author_details(client, author_id, api_url, headers):
    """_summary_

    Args:
        client: httpx client
        author_id: author id
        api_url: url will be used to call the api
        headers: request header object

    Returns:
        object: json response of the api call
    """
    author_details_response = await client.get(
        f"{api_url}/{author_id}",
        headers=headers,
        timeout=100
    )
    response = author_details_response.json()
    data = response.get("data", [])
    return data[0] if data else {}

async def prepare_content_list(
    author_ids,
    author_details_api_url,
    content_list_data,
    existing_authors_list,
    ):
    """fetch user details data and modify the content list response

    Args:
        author_ids (list): author id list
        author_details_api_url (string): author details api url
        content_list_data (list): content list

    Returns:
        dict: modified object with author details
    """
    # Fetch content list from the first third-party API
    async with httpx.AsyncClient() as client:

        # Fetch author details asynchronously for each content
        author_details_tasks = [
            get_author_details(
                client, author_id, author_details_api_url, get_request_headers()
            )
            for author_id in author_ids
        ]
        author_details = await asyncio.gather(*author_details_tasks)
    author_details = author_details + existing_authors_list

    # Extend content dictionaries with author details
    for content, details in zip(content_list_data, author_details):
        author_id = content["author"]["id"]
        content["author_details"] = get_dict_by_field_value(author_details, "unique_id", author_id)
    return content_list_data, author_details

def get_data_from_third_party_api(page=1):
    content_list_api_url_path = f"backend/api/v1/contents?page={page}"
    author_details_api_url_path = "backend/api/v1/authors/"
    content_list_api_url = generate_full_api_url(content_list_api_url_path)
    author_details_api_url = generate_full_api_url(author_details_api_url_path)
    response = requests.get(content_list_api_url, headers=get_request_headers())
    data = response.json()
    content_list_data = data.get("data", [])
    author_ids = list(map(lambda item: item["author"]["id"], content_list_data))
    existing_authors_qs = Author.objects.filter(unique_id__in=author_ids)
    existing_authors_unique_id_list = list(existing_authors_qs.values_list("unique_id", flat=True))
    missing_author_in_db = set(author_ids) - set(existing_authors_unique_id_list)
    existing_authors_list = list(existing_authors_qs.values_list("data", flat=True))
    results, author_details = asyncio.run(prepare_content_list(
        missing_author_in_db,
        author_details_api_url,
        content_list_data,
        existing_authors_list,
    ))
    data["data"] = results
    # Create or update authors using celery
    create_or_update_authors_lazy.delay(author_details)
    # sync_author_from_api_lazy.apply_async(
    #     (existing_authors_unique_id_list, author_details_api_url),
    #     countdown=3,
    #     retry=True, retry_policy={
    #         'max_retries': 10,
    #         'interval_start': 0,
    #         'interval_step': 0.2,
    #         'interval_max': 0.2,
    #     }
    # )
    return data
