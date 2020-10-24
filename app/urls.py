from django.urls import path, include
from . import views



urlpatterns = [
    path('niscaly', views.niscaly, name='niscaly'),
    path('niscaly_pos', views.posiciones, name='niscaly_pos'),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]