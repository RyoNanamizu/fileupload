from django.urls import path
from . import views

urlpatterns = [
    # path('', views.upload_file, name='upload_file'),
    path('', views.upload,name='upload'),
    
    # path('file', views.upload_file_js, name='upload_file_js'),
    path('success', views.success, name='success'),
]