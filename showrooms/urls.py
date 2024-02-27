from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name='carts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carts/', include('carts.urls', namespace='carts')),
    path('accounts/', include('django.contrib.auth.urls')),

    # other URL patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




