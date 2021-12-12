from django.urls import path
from . import views

urlpatterns = [
    path('', views.title, name='title'),
    path('top/', views.top, name='top'),
    path('freever/top/', views.index, name='f_top'),
    path('paidver/top/', views.ptop, name='p_top'),
    path('paidver/signup/', views.signup, name='signup'),
    path('paidver/login/', views.signin, name='login'),
    path('paidver/logout/', views.logout_view, name='logout'),
    path('game/freequiz/', views.f_quiz, name='f_quiz'),
    path('game/paidquiz/', views.p_quiz, name='p_quiz'),
]
