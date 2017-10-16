from django.conf.urls import include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('index.urls', namespace='index')),
    url(r'^ealert/', include('ealert.urls', namespace='ealert')),
]
