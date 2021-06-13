from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, View
from .models import Item

class HomeView(ListView):
    model = Item
    paginate_by = 8
    template_name = 'socialaccount/home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


