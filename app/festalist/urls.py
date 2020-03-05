from django.urls import include, path

from festalist.apis import FestaListAPIView, FestaListDetailAPIView

urlpatterns_api_view = [
    path('festalist/', FestaListAPIView.as_view()),
    path('festalist/<int:pk>/', FestaListDetailAPIView.as_view()),
]

urlpatterns = [
    path('api-view/', include(urlpatterns_api_view)),
]
