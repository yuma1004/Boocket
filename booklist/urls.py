from django.urls import path
from . import views

app_name = "booklist"

urlpatterns = [
    path('', views.LandingTemplateView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/lists/', views.ListsListView.as_view(), name="lists_list"),
    path('home/lists/create/', views.ListCreateView.as_view(), name="lists_create"),
    path('home/lists/<int:pk>/', views.ListDetailView.as_view(), name="lists_detail"),
    path('home/lists/<int:pk>/update/', views.ListUpdateView.as_view(), name="lists_update"),
    path('home/lists/<int:pk>/delete/', views.ListDeleteView.as_view(), name="lists_delete"),
    path('home/cards/', views.CardListView.as_view(), name='cards_list'),
    path('home/cards/create/', views.CardCreateView.as_view(), name='cards_create'),
    path('home/cards/<int:pk>/', views.CardDetailView.as_view(), name='cards_detail'),
    path('home/cards/<int:pk>/update/', views.CardUpdateView.as_view(), name='cards_update'),
    path('home/cards/<int:pk>/delete/', views.CardDeleteView.as_view(), name='cards_delete'),
    path('home/cards/create/<int:list_pk>', views.CardCreateFromHomeView.as_view(), name="cards_create_from_home"),
    path('home/cards/<int:pk>/update/<int:list_pk>', views.CardUpdateFromHomeView.as_view(), name="cards_update_from_home"),
]
