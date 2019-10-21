from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path
from users import urls
urlpatterns = [
    # Examples:
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'), name='register')
]
