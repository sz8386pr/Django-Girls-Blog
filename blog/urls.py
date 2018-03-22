from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # default
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),     # post details page using post pk as the url. /post/pk
    url(r'^post/new/$', views.post_new, name='post_new'),       # new post
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),    # updating post. post/post pk/edit/
]
