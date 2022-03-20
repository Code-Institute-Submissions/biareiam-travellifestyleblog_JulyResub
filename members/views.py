""" Libraries """
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from travellifestyleblog22.models import Profile
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib import messages


class CreateProfilePageView(CreateView):
    """ Create user profile """
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageview(generic.UpdateView):
    """ Edit user profile """
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    form_class = ProfilePageForm
    success_url = reverse_lazy('home')


class ShowProfilePageview(DetailView):
    """ Show user profile """
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageview, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    """ Change password """
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    """ redirect to the registraion successful page """
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    """ Show registration form """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, f'Account created successfully')
        return super().form_valid(form)


class UserEditView(generic.UpdateView):
    """ Edit settings"""
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
