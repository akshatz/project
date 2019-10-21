from django.conf.urls import include, url

from project import views, settings
from .settings import LOGOUT_REDIRECT_URL
from django.contrib import admin
from django.urls import path
from users import urls
from .views import *
urlpatterns = [
    # Examples:
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'), name='users'),
    path('logout/', views.logout_view, name='logout')
]
