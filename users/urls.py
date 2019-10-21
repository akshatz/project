from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('users/', views.register_view),
]