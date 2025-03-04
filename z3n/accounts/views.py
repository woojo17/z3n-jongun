
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages  # Django messages framework 추가
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "회원가입이 성공적으로 완료되었습니다!")  # 성공 메시지
            return redirect('home')  # 홈 페이지로 이동
        else:
            messages.error(request, "회원가입에 실패했습니다. 입력 정보를 다시 확인해주세요.")  # 실패 메시지
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'home'  # 로그아웃 후 리디렉션


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 회원가입 후 홈으로 이동
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
