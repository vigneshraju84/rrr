from django.urls import path
from cbv.views import BookAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('books/<int:id>', BookAPIView.as_view()),
]