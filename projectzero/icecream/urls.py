from django.urls import path
from . import views

urlpatterns = [
    path('', views.icecream_list, name='icecream-list'),
    path('<int:pk>/', views.icecream_detail, name='detail'),
    path('<str:username>/unfollow/', views.profile_unfollow, name='profile_unfollow'),
    path('<str:username>/follow/', views.profile_follow, name='profile_follow'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:pk>/unfav/', views.favourite_unfollow, name='favourite_unfollow'),
    path('<str:pk>/fav/', views.favourite_follow, name='favourite_follow'),
]

