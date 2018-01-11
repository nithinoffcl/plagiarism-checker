from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
	url(r'^plagiarism/',views.check,name = 'check'),
    url(r'^plagchecker',views.geturls,name='geturls'),
	url(r'^upload/',views.upload_file,name='upload'),
    ]


#views.check
