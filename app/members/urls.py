from django.urls import path

from members.apis import AuthTokenAPIView, CreateUserAPIView

urlpatterns = [
    path('auth-token/', AuthTokenAPIView.as_view()),
    path('create-user/', CreateUserAPIView.as_view())
]
