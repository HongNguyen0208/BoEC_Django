from django.urls import path
from .views import (
    HomeView, 
    ItemDetailView, 
    OrderSummaryView, 
    DetailView,
    add_to_cart,
    remove_single_item_from_cart,
)
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin


app_name = 'proshop'

urlpatterns = [
    path('', HomeView.as_view()),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
]



if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
    urlpatterns += [
        url(r'^admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


