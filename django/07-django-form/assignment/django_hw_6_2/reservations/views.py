from django.shortcuts import render,redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new_view(request):
    form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/new.html', context)

def create(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    form = ReservationForm(request.POST)
    if form.is_valid(): # 실패시 context에 실패이유
        Reservation = form.save()
        return redirect('reservations:index', Reservation.pk)
    # article = Article(title=title, content=content)
    # article.save()
    context = {
        'form': form,
    }
    # 실패한 이유 들어감. 위에 form과는 다른 놈
    return render(request, 'reservations/new.html',context)
    # redirect 아닌 이유. 에러가 담긴 form을 넘길 수가 없음. 에러메세지가 안뜸



