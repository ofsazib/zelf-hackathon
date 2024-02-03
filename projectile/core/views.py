from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from core.utils import get_data_from_third_party_api

class ZelfHackContentListApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            page = self.request.query_params.get("page", 1)
            data = get_data_from_third_party_api(page=page)
            return Response(data)

        except Exception as exception:
            return Response(
                {'error': f'Failed to fetch data from the API. {str(exception)}'},
                status=HTTP_400_BAD_REQUEST
            )
