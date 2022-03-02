from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageview, EditProfilePageview, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('settings/', UserEditView.as_view(), name='setting'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageview.as_view(), name='profile'),
    path('<int:pk>/edit/profile_page/', EditProfilePageview.as_view(), name='edit_profile'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create_profile'),
    ]
