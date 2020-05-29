from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'photos'

urlpatterns=[
    url('^$', views.home, name = 'home'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^myprofile$',views.myprofile,name='myprofile'),
    url(r'myprofile/edit$',views.edit,name='edit'),
    url(r"^search/",views.search,name="search"),

]