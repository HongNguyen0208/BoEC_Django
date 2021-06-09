from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control alternative'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control alternative'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-control alternative'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-control alternative'}))
    


class LoginForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())