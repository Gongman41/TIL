from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
app_name = 'articles'

# Create your views here.
def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('todos:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)
    
def detail(request, Article_pk):
    article = Article.objects.get(pk=Article_pk)
    context = {
        'article': article
    }
    return render(request, 'todos/detail.html', context)
