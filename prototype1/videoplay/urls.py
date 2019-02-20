#from videoplay.views import PlayView
from django.urls import path, re_path
from. import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='videoplay-home'),
    path('download/',views.download,name='videoplay-download'),
    #regex for appending query 
    #re_path(r'^videos/(?:score-(?P<score>\d+)/)?$',views.play, name='videoplay-videos')
    path('videos/',views.play,name='videoplay-videos')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#PlayView.as_view()
