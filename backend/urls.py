from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products', include('base.urls.product_urls')),
    path('api/users', include('base.urls.user_urls'))
]
