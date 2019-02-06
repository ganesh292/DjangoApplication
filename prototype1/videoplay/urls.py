from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='videoplay-home'),
    path('download/',views.download,name='videoplay-download'),
    path('videos/',views.videos,name='videoplay-videos')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
