from django.urls import path

from members import views

app_name = 'members'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]