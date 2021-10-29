from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import csv
import codecs

from django.views import View


from books.models import Book

count = 0
count_author = 0

def main_page(request):
    return render(request, "books/index.html")

@login_required()
def load_file(request):
    csv_file = csv.DictReader(codecs.iterdecode(request.FILES['file'], 'utf-8-sig'))
    book = Book.objects.all()
    context = {"book": book}
    for i in csv_file:
        key = (list(i.keys()))
        if Book.objects.filter(author=i[key[1]]).exists() and Book.objects.filter(book_title=i[key[2]]).exists() == False or \
            Book.objects.filter(author=i[key[1]]).exists() == False and Book.objects.filter(book_title=i[key[2]]).exists() or \
            Book.objects.filter(author=i[key[1]]).exists() == False and Book.objects.filter(book_title=i[key[2]]).exists() == False:
            Book.objects.create(author_birth_year=i[key[0]], author=i[key[1]], book_title=i[key[2]], book_written_year=i[key[3]])
            #Book.objects.create(author=i['Author'], book_title=i['BookTitle'], author_birth_year=i['AuthorBirthYear'], book_written_year=i['BookWrittenYear'])
    return render(request, "books/index.html", context)

def sort_birth(request):
    global count
    if count == 0:
        book = Book.objects.order_by("author_birth_year")
        count = 1
    else:
        book = Book.objects.order_by("-author_birth_year")
        count = 0
    context = {"book": book}
    return render(request, "books/index.html", context)

def sort_written_year(request):
    global count_author
    if count_author == 0:
        book = Book.objects.order_by("book_written_year")
        count_author = 1
    else:
        book = Book.objects.order_by("-book_written_year")
        count_author = 0
    context = {"book": book}
    return render(request, "books/index.html", context)

class LoginView(View):
    def get(self, request):
        return render(request, "books/login.html")
    def post(self, request):
        user = authenticate(
            username=request.POST['login'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect("main-page")
        return redirect("login")


def logout_view(request):
    logout(request)
    return redirect("main-page")


