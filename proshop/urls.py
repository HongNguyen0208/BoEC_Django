from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('index/', views.index, name='index'),
    url('signup/', views.signup, name='signup'),
    url('login/', views.login, name='login'),
    url('password_change/', views.password_change, name='password_change'),
    url('(?P<item_id>[0-9]+)/', views.detail, name='detail'),
]