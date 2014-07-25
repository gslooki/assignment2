from django.conf.urls import patterns, url, include
from my_social_network import views

urlpatterns = patterns('',
    # Examples:d myls
    # url(r'^$', 'assignment1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.homepage, name = 'homepage'),
    url(r'^users/$', views.users, name='users'),
    url(r'^(?P<username>\w+)/$', views.username, name = 'username'),
    url(r'^(?P<username>\w+)/followers/', views.usernamefollowers, name = 'followers'),
    url(r'^(?P<username>\w+)/following/', views.username, name = 'following'),
                       
)
