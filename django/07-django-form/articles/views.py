from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     form = ArticleForm(request.POST)
#     if form.is_valid(): # 실패시 context에 실패이유
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     # article = Article(title=title, content=content)
#     # article.save()
#     context = {
#         'form': form,
#     }
#     # 실패한 이유 들어감. 위에 form과는 다른 놈
#     return render(request, 'articles/new.html',context)
#     # redirect 아닌 이유. 에러가 담긴 form을 넘길 수가 없음. 에러메세지가 안뜸

    
def create(request):
    form = ArticleForm(request.POST)
    if request.method == 'POST':
        if form.is_valid(): # 실패시 context에 실패이유
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: # POST가 아닌 모든 경우 <->GET이 아닌 모든 경우
        form = ArticleForm()
    context = {
        'form':form,
    }
    # 이 위치에 이 들여쓰기여야 에러메세지를 포함
    return render(request,'article/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     # 기존 객체의 정보
#     context = {
#         'article': article,
#         'form':form
#     }
#     return render(request, 'articles/edit.html', context)
# # GET

# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(request.POST,instance=article)
#     # 기존 객체 넣어주면 수정
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')

#     # article.title = title
#     # article.content = content
#     # article.save()
#     if form.is_valid():
#         form.save()
#         return redirect("articles:detail",article.pk)
#     context = {
#         'form':form,
#         'article':article,
#     }
#     return render(request,'articles/edit.html', context)
#     # 생성 수정 구분.
# # POST

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
    else:
        form ...
            
