from django.urls import path
from books import views

urlpatterns = [
    path('', views.main_page,name='main-page'),
    path('load_file/', views.load_file, name='load_file'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("sort_birth/", views.sort_birth, name='sort-birth'),
    path("sort_written_year/", views.sort_written_year, name='sort-written-year'),
]