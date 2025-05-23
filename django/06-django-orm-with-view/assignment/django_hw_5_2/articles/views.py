from django.shortcuts import render,redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request,'articles/new.html')
    

def create(request):
    # request.GET
    title = request.POST.get('title')
    content = request.POST.get('content')
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    article = Article(title=title, content=content)
    article.save()
# 유효성 검증때문에
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    return redirect('articles:index')