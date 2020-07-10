from django.urls import path, include

from . import views

app_name = 'vk_bot'

urlpatterns = [
    path('', views.index, name='index'),

]