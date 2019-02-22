from django.urls import path
from . import views

urlpatterns = \
    [
        path('', views.index, name='index'),
        path('index/', views.indexDirection, name='indexDirection'),
        path('base/', views.Base, name='Base'),
        path('about/', views.About, name='About')
    ]
