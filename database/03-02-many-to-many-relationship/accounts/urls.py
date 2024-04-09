from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<str:username>/',views.profile,name='profile'),
    # 첫번째에 username을 넣으면 밑에 주소가 다 죽음. 
    path('<int:user_pk>/follow',views.follow,name = 'follow')
]
