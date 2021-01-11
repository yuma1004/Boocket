from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ListForm, CardForm, CardFromHomeForm
from . models import List, Card

# ランディングページ
class LandingTemplateView(TemplateView):
    template_name = 'booklist/index.html'

# ホームページ（サインアップ完了画面）
class HomeView(LoginRequiredMixin, ListView):
    model = List
    template_name = 'booklist/home.html'

# カード作成
class CardCreateFromHomeView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "booklist/cards/create.html"
    form_class = CardFromHomeForm
    success_url = reverse_lazy("booklist:home")

    def form_valid(self, form):
        list_pk = self.kwargs['list_pk']
        list_instance = get_object_or_404(List, pk=list_pk)
        form.instance.list = list_instance
        form.instance.user = self.request.user
        return super().form_valid(form)

# カード編集
class CardUpdateFromHomeView(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = "booklist/cards/update.html"
    form_class = CardFromHomeForm

    def get_success_url(self):
        return resolve_url('booklist:home')



# ブックリスト：作成ページ
class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "booklist/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("booklist:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# ブックリスト：閲覧ページ
class ListsListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "booklist/lists/list.html"

# ブックリスト：詳細ページ
class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = "booklist/lists/detail.html"

# ブックリスト：編集ページ
class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "booklist/lists/update.html"
    form_class = ListForm

    def get_success_url(self):
        return resolve_url('booklist:home')

# ブックリスト：削除ページ
class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "booklist/lists/delete.html"
    form_class = CardFromHomeForm
    success_url = reverse_lazy("booklist:home")



# ブックリストカード：作成ページ
class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "booklist/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("booklist:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# ブックリストカード：閲覧ページ
class CardListView(LoginRequiredMixin, ListView):
    model = Card
    # template_name = "booklist/cards/list.html"


# ブックリストカード：詳細ページ
class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = "booklist/cards/detail.html"

# ブックリストカード：編集ページ
class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = "booklist/cards/update.html"
    form_class = CardForm
    
    def get_success_url(self):
        return resolve_url('booklist:cards_detail', pk=self.kwargs['pk'])

# ブックリストカード：削除ページ
class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = "booklist/cards/delete.html"
    form_class = CardForm
    success_url = reverse_lazy('booklist:home')
