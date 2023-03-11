from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('image_cls_module.urls')),
    path('admin/', admin.site.urls),
]