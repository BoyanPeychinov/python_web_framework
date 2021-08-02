from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from pythons.pythons_auth.forms import SignInForm, SignUpForm

UserModel = get_user_model()


# def sign_up(request):
#     if request.POST:
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = SignUpForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign_up.html', context)


class SignUpView(CreateView):
    template_name = 'auth/sign_up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('index')


# def sign_in(request):
#     # user = authenticate(username='Boyan', password='167943')
#     # login(request, user)
#     # return redirect('index')
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#
#     else:
#         form = SignInForm()
#
#         context = {
#             'form': form,
#         }
#
#     return render(request, 'auth/sign_in.html', context)


class SignInView(LoginView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('index')


def sign_out(request):
    logout(request)
    return redirect('index')
