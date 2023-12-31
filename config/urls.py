from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from config.views import index_view

urlpatterns = [
    path('', index_view, name='home'),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)