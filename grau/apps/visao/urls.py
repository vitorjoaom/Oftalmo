from django.urls import path
from apps.visao.views import index, home

urlpatterns = [
    path('', index, name=index),
    path('', home, name=home),
]