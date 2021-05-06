from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('actor_profile/', views.actor_profile_page, name='actor_profile'),
    path('employer_profile/', views.employer_profile_page, name='employer_profile'),
    path('actors/', views.actors_page, name='actors'),
    path('roles/', views.roles_page, name='roles'),
    path('role/<int:role_id>/', views.role_page, name='role')
]
