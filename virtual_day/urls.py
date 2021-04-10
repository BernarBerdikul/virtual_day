from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('super_secret_admin/', admin.site.urls, name='admin'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api_client/', include('api_client.urls')),
    path('api_console/', include('api_console.urls')),
    path('chat/', include('virtual_day.chat.urls')),
    prefix_default_language=False,
)

urlpatterns += path('chat/', include('virtual_day.chat.urls')),

# API Docs of DRF will be shown only on test mode
if settings.IS_TEST:
    urlpatterns += [
        url(r'^api/docs/', include_docs_urls(title='virtual_day documentation',
                                             authentication_classes=[],
                                             permission_classes=[permissions.AllowAny])),
    ]
if settings.IS_LOCAL:
    # This will be used when we launch this locally by runserver
    # On remote server it should be handled by Nginx
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
