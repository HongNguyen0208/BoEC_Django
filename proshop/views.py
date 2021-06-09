from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.contrib.auth.models import User

def home(request):
    return render(request, 'proshop/home.html')
    
def index(request):
    cus = get_object_or_404(User, id=request.user.id)
    return render(request,'proshop/index.html', {'sub': cus})

def detail(request, item_id):
    return HttpResponse("You are looking at item %s" % item_id)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session.set_expiry(0)
                auth_login(request, user)
                return HttpResponseRedirect('/proshop/index')
    else:
        form = LoginForm()

    return render(request, 'proshop/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, "proshop/signup.html", {
                    'form' : form,
                    'error_message' : 'Username already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, "proshop/signup.html", {
                    'form' : form,
                    'error_message' : 'Password do not match.'
                })
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                user.save()

                auth_login(request, user)

                return HttpResponseRedirect('/proshop')
                
    
    else:
        form = SignUpForm()

    return render(request, "proshop/signup.html", {'form': form})

def password_change(request):
    return render(request, "proshop/password_change.html")