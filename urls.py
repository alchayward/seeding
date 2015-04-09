from django.conf.urls import patterns, url
from seeding import views

urlpatterns = patterns('',
    url(r'^$', views.tournament_list),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^tournaments/(?P<tournament_id>\d+)/[\w -]+/(?P<session_name>[\w -]+)/$',
         views.session),
    url(r'^tournaments/(?P<tournament_id>\d+)/[\w -]+/$',
         views.tournament),
    url(r'^tournaments/$', views.tournament_list),
    url(r'^tournaments/(?P<tournament_name>\w+)/teams/$',
        views.team_list),
)

    


