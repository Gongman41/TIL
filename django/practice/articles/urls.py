from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # url->view->template
    path('',views.index, name = 'index'),
]