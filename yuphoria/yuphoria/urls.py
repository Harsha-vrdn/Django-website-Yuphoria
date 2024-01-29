
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path("user_login/", include("user_login.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("cart/", include("cart.urls")),
    path("makeit/", include("main.urls")),
]
