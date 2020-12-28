from django.urls import path
from django.contrib.auth import  views as auth_views
from.import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logOutUser, name='logout'),
    path('', views.home, name='home'),
     path('user/', views.user, name='user'),
    path('create_person/', views.create_person,name='create_person'),
    path('base/', views.base, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('seach2/', views.seach2, name='seach2'),
    path('update_person/<int:id>/', views.update_person, name='update_person'),
    path('delete_person/<int:id>/', views.delete_person, name='delete_person'),   



    #Password Reset urls
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='myapp/reset_password.html'),
    name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_comlete.html'), name='password_reset_complete'),

]