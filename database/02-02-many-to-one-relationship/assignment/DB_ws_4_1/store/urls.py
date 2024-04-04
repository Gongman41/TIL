
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:store_pk>/detail/',views.detail,name='detail'),
]
