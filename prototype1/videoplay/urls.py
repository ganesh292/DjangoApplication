from django.urls import path, re_path
from. import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='videoplay-home'),
    re_path('download/', views.download,name='videoplay-download'), 
    path('temp/',views.temp, name='score-collection'),
    path('videos/', views.play, name='videoplay-videos'),
    path('videos2/', views.play2, name='videoplay-videos2')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
