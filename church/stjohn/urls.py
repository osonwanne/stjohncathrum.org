from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stjohn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # News
    url(r'^news/', include('blanc_basic_news.urls', namespace='blanc_basic_news')),

    # Events
    url(r'^events/', include('blanc_basic_events.urls', namespace='blanc_basic_events')),
)

# Serving media under debug
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
