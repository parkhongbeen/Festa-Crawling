from django.urls import path
from members import views
from members.apis import AuthTokenAPIView, CreateUserAPIView

urlpatterns = [
    path('auth-token/', AuthTokenAPIView.as_view()),
    path('create-user/', CreateUserAPIView.as_view()),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
