from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('authority-dashboard/', views.authority_dashboard, name='authority_dashboard'),
]