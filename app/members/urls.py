from django.urls import path

from members.apis import AuthTokenAPIView, CreateUserAPIView, LogoutAPIView, CheckUserAPIView, GetUserInfoAPIView

urlpatterns = [
    path('get-user/', GetUserInfoAPIView.as_view()),
    path('check-user/', CheckUserAPIView.as_view()),
    path('auth-token/', AuthTokenAPIView.as_view()),
    path('create-user/', CreateUserAPIView.as_view()),
    path('logout-user/', LogoutAPIView.as_view())
]
