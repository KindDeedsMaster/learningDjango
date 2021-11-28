from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('onemore/', views.notindex, name = 'namenotindex')
]