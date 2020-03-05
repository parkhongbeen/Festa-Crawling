from django.urls import include, path
from festalist.apis import api_view

app_name = 'festalist'

urlpatterns_api_view = [
    path('festalist/', api_view.SnippetListCreateAPIView.as_view()),
    path('festalist/<int:pk>/', api_view.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]

urlpatterns = [
    path('api-view/', include(urlpatterns_api_view)),
]
