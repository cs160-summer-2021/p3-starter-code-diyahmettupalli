from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('a', views.a, name='a'),
    path('b', views.b, name='b'),
    path('c', views.c, name='c'),
    path('d', views.d, name='d'),
    path('e', views.e, name='e'),
    path('f', views.f, name='f'),
    path('g', views.g, name='g'),
    path('h', views.h, name='h'),
    path('i', views.i, name='i'),
    path('k', views.k, name='k')

]
