from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.permissions import AllowAny
from .serializers import ContentWriteSerializer, ContentBulkWriteSerializer
from .models import Content

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


class ContentListApiView(ListAPIView):
    serializer_class = ContentWriteSerializer
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return Content.objects.all().order_by("-pk")

class ContentCreateApiView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            data = data.get("data", [])
            serializer = ContentWriteSerializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as exception:
            return Response(
                {'error': f'Failed to create content. {str(exception)}'},
                status=HTTP_400_BAD_REQUEST
            )
