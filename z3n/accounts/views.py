from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 자동 로그인
            return redirect('home')  # 회원가입 후 이동할 페이지
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})
