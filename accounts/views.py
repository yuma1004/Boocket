from django.shortcuts import render, redirect, resolve_url
from django.views import generic
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserForm


# サインアップ画面
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("booklist:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'accounts/signup.html', context)

# ユーザー詳細画面
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/users/detail.html"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "accounts/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('accounts:users_detail', pk=self.kwargs['pk'])
