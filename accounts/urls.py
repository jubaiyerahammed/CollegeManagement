from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"


urlpatterns = [
    path('li/', views.login_view, name='login_view'),
    path('lo/', views.logout_view, name='logout'),
    path('rs/', views.register_student, name='register_student'),
    path('rt/', views.register_teacher, name='register_teacher'),
    
    path('menu/',views.menu, name="menu"),
    path('withdraw/',views.withdraw, name="withdraw"),
    path('deposit/', views.deposit, name="deposit"),
    path('balance/',views.balance, name="balance"),
    # Login
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html"
    ), name="login"),

    # Logout
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Registration
    path("register/", views.register, name="register"),

    # Change password
    path("password/change/", auth_views.PasswordChangeView.as_view(
        template_name="accounts/password_change.html"
    ), name="password_change"),
    path("password/change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="accounts/password_change_done.html"
    ), name="password_change_done"),
    # Forgot password (reset)
    path("password/reset/", auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"
    ), name="password_reset"),
    path("password/reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_done"),
    path("password/reset/confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html"
    ), name="password_reset_confirm"),
    path("password/reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ), name="password_reset_complete"),
    path("profile/", views.profile, name="profile"),
    path("my-account/", views.my_account, name="my_account"),

]    