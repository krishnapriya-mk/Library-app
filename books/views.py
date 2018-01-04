from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Book,Author
from .forms import AuthorForm,BookForm

class authordetail(View):
    template_name='authordetail.html'
    def get(self,request,author_id):

        context={
            'author':Author.objects.get(id=author_id)
        }
        return render(request, self.template_name, context)

class bookdetail(View):
    template_name='bookdetail.html'
    def get(self,request,book_id):
        t=Book.objects.get(id=book_id)
        context = {
            'book':t,
            'author':t.author_id,
        }
        return render(request, self.template_name, context)

class Index(View):
    template_name = 'index.html'
    def get(self,request):
        context={
            'Books':Book.objects.all()[::-1],
            'numberofbooks':len(Book.objects.all()),
            'bform':BookForm,
                 }

        return render(request, self.template_name,context)
    def post(self,request):
        B = BookForm(request.POST)
        if B.is_valid():
            object = B.save()
            #print object
        return redirect(reverse('book'))
class authorView(View):
    template_name='authors.html'
    def get(self,request):
        context={
            'aform': AuthorForm,
            'authors':Author.objects.all()[::-1],
            'numberofauthors':len(Author.objects.all()),
        }
        return render(request,self.template_name,context)

    def post(self, request):
        A = AuthorForm(request.POST or None)
        if A.is_valid():
            object = A.save()
            #print object
        return redirect(reverse('author'))



