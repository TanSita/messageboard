from django.conf.urls import patterns, include, url
from .views import * #把app的views import 進來

urlpatterns = patterns('',
    url(r'^$', show_messages),
)
# {}
