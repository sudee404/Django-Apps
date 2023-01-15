from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path("", views.login_view, name='home'),  # User login
    path("login/",views.login_view,name='login' ),  # User login
    path("registration/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path('password_reset/', views.MyPasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
