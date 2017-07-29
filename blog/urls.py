from  django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post$', views.post, name='post'),
    url(r'^$', views.home, name='home'),
]
