from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article,Comment
from .forms import ArticleForm,CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 특정 게시글에 작성된 모든 댓글 조회
    comments = article.comment_set.all()
    # Comment.objects.all() 은 데이터 베이스의 모든 댓글 조회
    comment_form = CommentForm()


    context = {
        'article': article,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request,pk):
    # 게시글 조회 ( 어떤 게시글에 작성되어야 하는지)
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    # 사용자 입력 데이터를 받아서 Comment 저장. 여기는 POST만 옴 -> else 필없
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # 저장이 이루어지기 전에 comment 인스턴스를 제공받는게 필요
        # save 메서드의 commit 속성. DB에 저장하지않고 인스턴스만 반환
        comment.article = article
        comment.save()
        return redirect('articles:detail',article.pk)
    context = {
        'comment_form':comment_form,
        'article':article,
        'comments':comments,
    }
    return render(request,'articles/detail.html',context)
#  NoReverseMatch. 현재 페이지의 url태그만 보면됨

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk 도 가능
    # 단 이렇게 작성할경우 url구성 변경, url 전체구성 및 통일성 위해
    comment.delete()
    return redirect('articles:detail', article_pk)
