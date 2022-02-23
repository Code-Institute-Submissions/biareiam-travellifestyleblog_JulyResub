from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('settings/', UserEditView.as_view(), name="setting"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html")),
    path('password/', PasswordChangeView.as_view(template_name="registration/change_password.html")),
    path('password_success',views.password_success, name='password_success'),
    
]