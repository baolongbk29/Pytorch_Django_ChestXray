from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'image_cls_module'
urlpatterns = [
    # two paths: with or without given image
    path('predict/', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)