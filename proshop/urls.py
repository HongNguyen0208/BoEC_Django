from django.urls import path
from .views import (
    HomeView, 
    ItemDetailView
)
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path


app_name = 'proshop'

urlpatterns = [
    path('', HomeView.as_view()),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]



if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]