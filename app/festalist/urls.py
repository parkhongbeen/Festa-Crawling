from django.urls import include, path

from festalist.apis import FestaListAPIView, FestaListDetailAPIView, FestaListKeywordUpload

urlpatterns_api_view = [
    path('festalist/', FestaListAPIView.as_view()),
    path('festalist/<int:pk>/', FestaListDetailAPIView.as_view()),
    path('festalist/keyword/<int:pk>/', FestaListKeywordUpload.as_view())
]

urlpatterns = [
    path('api-view/', include(urlpatterns_api_view)),
]
