from django.urls import path
from .views import home, RegisterView, UserListView, UserDetailView, ExpenseSummaryView

urlpatterns = [
    path('', home),  # Add this for the root URL
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('expenses/summary/', ExpenseSummaryView.as_view(), name='expense-summary'),
]