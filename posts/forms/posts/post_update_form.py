from django import forms


class PostUpdateForm(forms.Form):
    id = forms.IntegerField()
    title = forms.CharField(max_length=100)
    body = forms.CharField(max_length=1000)