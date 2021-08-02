from django.urls import path

from pythons.pythons_auth import views
from pythons.pythons_auth.views import SignUpView, SignInView

urlpatterns = [
    # path('sign-up/', views.sign_up, name='sign up'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    # path('sign-in/', views.sign_in, name='sign in'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', views.sign_out, name='sign out'),
]
