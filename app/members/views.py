from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from members.forms import LoginForm, SignupForm


def index(request):
    return render(request, 'post/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('members:index')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'member/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('members:index')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('member:login')


# def Send_Eamil(reqeust):
#     email = EmailMessage(
#         'festa홈페이지에서 보내드립니다.',
#         'test4',
#         to=['pack122@naver.com', 'dhgudrms12@naver.com', 'dohyeonee95@hotmail.com', 'ghks130@naver.com'],
#     )
#     email.send()
