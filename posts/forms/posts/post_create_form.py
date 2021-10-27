from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(max_length=1000)