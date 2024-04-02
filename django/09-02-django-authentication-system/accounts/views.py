from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from.forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form =  CustomUserCreationForm(request.POST)
        # 에러. 상속 후 재정의. UserChangeForm도 재정의 필요
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form =  CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)
@login_required
def delete(request):
    # 삭제하고자하는 User를 조회할 필요 없다
    request.user.delete()
    return redirect('articles:index')
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)
# 옵션이 너무 많음. 일반 사용자가 너무 많은 컨트롤 가능
@login_required
def change_password(request,user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        # PasswordChangeForm은 첫번쨰 인자 user가 필수
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)