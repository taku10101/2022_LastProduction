
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
# from django.views.generic import TemplateView

# index_View= TemplateView.as_view(template_name="index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)