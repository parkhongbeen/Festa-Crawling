from django.urls import include, path

from festalist.apis import FestaListAPIView, FestaListDetailAPIView, FestaListKeywordUpload, FestaListKeywordDelete

urlpatterns = [
    # path('open-event/', FestaListOpenEventAPIView.as_view()), # 이메일발송 테스트용
    path('', FestaListAPIView.as_view()),
    path('<int:pk>/', FestaListDetailAPIView.as_view()),
    path('keyword/', FestaListKeywordUpload.as_view()),
    path('keyword/<int:pk>/', FestaListKeywordDelete.as_view())
]
