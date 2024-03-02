from django import forms
 
class BulletinForm(forms.Form):
    bulletin_name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    pic_field = forms.ImageField()

class PostForm(forms.Form):
    post_name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    pic_field = forms.ImageField()