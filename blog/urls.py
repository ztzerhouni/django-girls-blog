'''
URLS for the blog application within the djangogirls project.
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]