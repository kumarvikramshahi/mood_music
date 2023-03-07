from django.urls import path
from API.views import file_upload
from django.urls import path, include

urlpatterns = [
    path('upload/', file_upload, name='file_upload'),
    path('api/', include('api.urls')),
]
