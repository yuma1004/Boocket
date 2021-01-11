from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"),
]
