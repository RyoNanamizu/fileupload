from django.urls import path
from . import views

urlpatterns = [
    # path('', views.upload_file, name='upload_file'),
    path('', views.upload_file, name='upload_file'),
    path('success', views.success, name='success'),
]