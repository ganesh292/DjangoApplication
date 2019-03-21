from django.test import TestCase, Client
from django.urls import reverse,resolve
from videoplay.views import home,download
import json
# Create your tests here.

class Tests(TestCase):

#Testing URLs
    def test_videoplay_home_urlisresolved(self):
        url=reverse('videoplay-home')
        self.assertEquals(resolve(url).func,home)

    def test_videoplay_download_urlisresolved(self):
        url = reverse('videoplay-download')
        self.assertEquals(resolve(url).func, download)

#Testing Views
    def setUp(self):
        self.client=Client()
        self.home_url=reverse('videoplay-home')
        self.download_url=reverse('videoplay-download')


    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'videoplay/home.html')

    def test_download_GET(self):
        response = self.client.get(self.download_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'videoplay/download.html')
