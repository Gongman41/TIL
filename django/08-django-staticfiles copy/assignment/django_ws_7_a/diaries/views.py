from django.shortcuts import render,redirect
from .models import Diary_model
from .forms import DiaryForm
# Create your views here.

def index(request):
    Diary_model_list = Diary_model.objects.all()
    context = {
        'Diary_model_list': Diary_model_list
    }
    return render(request, 'diaries/index.html', context)
def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:index', diary.pk)
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)