from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .routers import router

admin.site.index_template = 'admin/index.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('api/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)