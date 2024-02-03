from django.urls import path
from core.views import ZelfHackContentListApiView

urlpatterns = [
    path('contents/', ZelfHackContentListApiView.as_view(), name='zelf-api-list'),
]
