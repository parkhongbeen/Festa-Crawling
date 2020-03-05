from django.urls import path
from members import views
from members.apis import AuthTokenAPIView, CreateUserAPIView, LogoutAPIView

urlpatterns = [
    path('auth-token/', AuthTokenAPIView.as_view()),
    path('create-user/', CreateUserAPIView.as_view()),
    path('logout-user/', LogoutAPIView.as_view())
]
