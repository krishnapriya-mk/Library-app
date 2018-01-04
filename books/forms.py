from django import forms
from django.forms import ModelForm
from . import models
class BookForm(ModelForm):
    class Meta:
        model = models.Book
        fields =['bookname','brief_description','description','author_id']

class AuthorForm(ModelForm):
    class Meta:
        model =models.Author
        fields=['authorname']