from django.urls import include, path

from festalist.apis import FestaListAPIView, FestaListDetailAPIView, FestaListKeywordUpload

urlpatterns = [
    path('', FestaListAPIView.as_view()),
    path('<int:pk>/', FestaListDetailAPIView.as_view()),
    path('keyword/', FestaListKeywordUpload.as_view())
]
