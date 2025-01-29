from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import ArticleFilter, CommentFilter, VideoFilter
from .models import (About, Article, Comment, PrivacyPolicy, Question,
                     SocialMedia, Subject, TermsOfService, Video)
from .serializers import (AboutSerializer, ArticleDetailSerializer,
                          ArticleListSerializer, CommentSerializer,
                          PrivacyPolicySerializer, QuestionSerializer,
                          SocialMediaSerializer, SubjectSerializer,
                          TermsOfServiceSerializer, VideoDetailSerializer,
                          VideoListSerializer)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = VideoFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return VideoListSerializer
        return VideoDetailSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class PrivacyPolicyViewSet(viewsets.ModelViewSet):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer


class TermsOfServiceViewSet(viewsets.ModelViewSet):
    queryset = TermsOfService.objects.all()
    serializer_class = TermsOfServiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
