from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('jumia/', include('my_jumia.urls')),
    path('admin/', admin.site.urls),
]
