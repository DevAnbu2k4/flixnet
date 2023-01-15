from django.urls import path
from . import views



urlpatterns=[
    path('', views.index, name='index'),
    path('search/', views.search_item, name='search'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('video/<str:pk>/', views.dynamic, name='video'),
    path('title/<str:pk>/', views.groupdyn, name='group'),
]