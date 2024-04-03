from django.shortcuts import render,redirect
from .models import Author,Book
from .forms import AuthorForm, BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    book_form = BookForm()
    context = {
        'author': author,
        'book_form':book_form,
        'books':books
    }
    return render(request, 'libraries/detail.html', context)

def create(request,author_pk):
    # 게시글 조회 ( 어떤 게시글에 작성되어야 하는지)
    author = Author.objects.get(pk=author_pk)
    books = Book.book_set.all()
    # 사용자 입력 데이터를 받아서 Comment 저장. 여기는 POST만 옴 -> else 필없
    book_form = BookForm(request.POST)
    if book_form.is_valid():
        book = book_form.save(commit=False)
        # 저장이 이루어지기 전에 comment 인스턴스를 제공받는게 필요
        # save 메서드의 commit 속성. DB에 저장하지않고 인스턴스만 반환
        book.author = author
        book.save()
        return redirect('libraries:detail',author.author_pk)
    context = {
        'book_form':book_form,
        'author':author,
        'books':books,
    }
    return render(request,'libraries/detail.html',context)

