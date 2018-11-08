from django.urls import path
from animation_manage import views

urlpatterns = [
    path(r'show_animation', views.show_animation, name='show_animation')
]
