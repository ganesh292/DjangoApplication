from django.urls import path, re_path
from. import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='videoplay-home'),
    re_path('download/', views.download,name='videoplay-download'), 
    path('temp/',views.temp, name='score-collection'),
    path('preference/',views.preference, name='score-preference'),
    path('videos/', views.play, name='videoplay-videos'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
