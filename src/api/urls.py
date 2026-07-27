from django.urls import path
from . import views

urlpatterns = [
    path('subrabbles', views.subrabble_list, name='subrabble-list'),
    path('subrabbles/!<str:identifier>', views.subrabble_detail, name='subrabble-detail'),
    path('subrabbles/!<str:identifier>/posts', views.subrabble_posts, name='subrabble-posts'),
    path('subrabbles/!<str:identifier>/posts/<int:pk>', views.post_detail, name='post-detail'),
]