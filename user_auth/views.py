from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from user_auth.models import MyUser
from .forms import RegisterForm, LoginForm, CustomSetPasswordForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'base_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, 'base_form.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')


class MyPasswordResetView(PasswordResetView):
    template_name = 'my_password_reset_form.html'
    email_template_name = 'my_password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = MyUser.objects.get(email=email)
            return super().form_valid(form)
        except MyUser.DoesNotExist:
            messages.warning(self.request, 'No user found with this email')
            return self.form_invalid(form)



class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'my_password_reset_done.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'my_password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    post_reset_login = True

    def form_valid(self, form):
        print("valid")
        form.save()
        return super().form_valid(form)




class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'my_password_reset_complete.html'
