#from videoplay.views import PlayView
from django.urls import path, re_path
from. import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='videoplay-home'),
    re_path('download/', views.download,name='videoplay-download'),
    #regex for appending query 
    path('temp/',views.temp, name='score-collection'),
    path('videos/', views.play, name='videoplay-videos'),
    #path('videos/', views.temp, name='score-collection')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#PlayView.as_view()
