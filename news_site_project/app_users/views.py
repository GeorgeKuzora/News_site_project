from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from app_users.forms import AuthForm, UserRegisterForm, UserEditForm
from app_users.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли в систему')
                else:
                    auth_form.add_error('__all__', 'Ошибка учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля')
    auth_form = AuthForm()
    context = {
            'form': auth_form
            }
    return render(request, 'app_users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из под своей учетной записи')


class UserRegisterView(View):
    def get(self, request):
        user_form = UserRegisterForm()
        return render(request, 'app_users/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            date_of_birth = user_form.cleaned_data.get('date_of_birth')
            city = user_form.cleaned_data.get('city')
            Profile.objects.create(
                    user=user,
                    city=city,
                    date_of_birth=date_of_birth,
                    )
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            user_form = UserRegisterForm()
        return render(request, 'app_users/register.html', {'user_form': user_form})


class UserEditView(View):
    def get(self, request):
        user = request.user
        user_form = UserEditForm(instance=user)
        return render(request, 'app_users/user_edit.html', context={'user_form': user_form})

    def post(self, request):
        user = request.user
        user_form = UserEditForm(request.POST, instance=user)
        if user_form.is_valid():
            user = user_form.save()
            date_of_birth = user_form.cleaned_data.get('date_of_birth')
            city = user_form.cleaned_data.get('city')
            verification_mark = user_form.cleaned_data.get('verification_mark')
            Profile.user=user.username,
            Profile.city=city,
            Profile.date_of_birth=date_of_birth,
            Profile.verification_mark=verification_mark,
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/edit')
        return render(request, 'app_users/user_edit.html', context={'user_form': user_form})
