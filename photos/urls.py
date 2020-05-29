from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns=[
    url('^$', views.home, name = 'home'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^myprofile$',views.myprofile,name='myprofile'),
    url(r'myprofile/edit$',views.edit,name='edit'),
    url(r'image/comment/(\d+)/$',views.comments,name='comment'),
    url(r'profile/user/(\d+)/$',views.profile,name='users'),
    url(r"^search/",views.search,name="search"),

]
