from django.conf.urls import include, url
from django.contrib import admin

from chatbot.views import MyChatBotView, index
from dashboard.views import index as dashboard_index
from dashboard.views import login,web

urlpatterns = [
    # Examples:
    # url(r'^$', 'codingblocks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook_auth/?$', MyChatBotView.as_view()),
    url(r'^$',index),
    url(r'^dashboard/?$',dashboard_index),
    url(r'^login/?$',login),
    url(r'^web/?$',web),
]
