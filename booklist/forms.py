from django import forms
from django.contrib.auth.models import User

from .models import List, Card


class ListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'2020.6'
    }))

    class Meta:
        model = List
        fields = ("title",)


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description", "list")


class CardFromHomeForm(forms.ModelForm):

    no = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'12345'
    }))
    status = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'読了'
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'7つの習慣'
    }))
    author_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'スティーブン・R・コヴィー'
    }))
    category = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'自己啓発'
    }))
    motive = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'成功するための習慣を知りたい'
    }))
    issuance_years = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'2013年'
    }))
    class Meta:
        model = Card
        fields = ("no", "status", "title", "author_name", "category", "motive", "issuance_years")
