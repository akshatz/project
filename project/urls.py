from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path
from registration import urls
urlpatterns = [
    # Examples:
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls'), name='register')
]
