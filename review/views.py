from datetime import datetime

from rest_framework import viewsets, mixins, generics, views
# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny

from review.serializers import CreateReviewSerializer, UpdateReviewSerializer, \
    CreateQuestionSerializer, UpdateQuestionSerializer, CreateAnswerSerializer
from review.models import Review, Question, Answer


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return CreateReviewSerializer(*args, **kwargs)
        elif self.action == 'update':
            return UpdateReviewSerializer(*args, **kwargs)


class QuestionViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return CreateQuestionSerializer(*args, **kwargs)
        elif self.action == 'update':
            return UpdateQuestionSerializer(*args, **kwargs)


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.filter(start_date__lte=datetime.today(), end_date__gte=datetime.today())
    serializer_class = UpdateReviewSerializer


class AnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = CreateAnswerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"session": self.request.session.session_key})
        return context
