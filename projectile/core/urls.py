from django.urls import path
from core.views import ZelfHackContentListApiView, ContentListApiView, ContentCreateApiView

urlpatterns = [
    path('contents/', ZelfHackContentListApiView.as_view(), name='zelf-api-list'),
    path('contents/list', ContentListApiView.as_view(), name='content-list'),
    path('contents/create', ContentCreateApiView.as_view(), name='content-create'),
]
