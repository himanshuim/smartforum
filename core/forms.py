from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class BlogForm(forms.Form):
    title = forms.CharField()
    message = forms.CharField()