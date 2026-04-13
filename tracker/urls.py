from django.urls import path
from . import views
from . import auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('delete/<int:id>/', views.delete_transaction, name='delete_transaction'),
    path('edit/<int:id>/', views.edit_transaction, name='edit_transaction'),

    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register_view, name='register'),
    path('logout/', auth_views.logout_view, name='logout'),
]