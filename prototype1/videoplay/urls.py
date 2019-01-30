from django.urls import path
from. import views


urlpatterns = [
    path('', views.home,name='videoplay-home'),
    path('download/',views.download,name='videoplay-download'),
    path('download/file',views.filedownload,name='videoplay-filedownload'),
    path('videos/',views.videos,name='videoplay-videos')

]