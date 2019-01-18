from django.urls import path
from. import views


urlpatterns = [
    path('', views.home,name='videoplay-home'),
    path('videos/',views.videos,name='videoplay-videos')
]