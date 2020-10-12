from django.urls import path
from rest_framework.routers import DefaultRouter

from review.views import ReviewViewSet, QuestionViewSet, ReviewListView, AnswerView

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'questions', QuestionViewSet, basename='question')


urlpatterns = router.urls + \
[
    path('reviews/active', ReviewListView.as_view()),
    path('reviews/answer', AnswerView.as_view()),
]