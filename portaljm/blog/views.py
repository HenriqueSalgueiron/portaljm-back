# viewSet vs ModelView

from rest_framework import viewsets

from .models import (About, Article, Comment, PrivacyPolicy, Question,
                     SocialMedia, TermsOfService, Video)
from .serializers import (AboutSerializer, ArticleDetailSerializer,
                          ArticleListSerializer, CommentSerializer,
                          PrivacyPolicySerializer, QuestionSerializer,
                          SocialMediaSerializer, TermsOfServiceSerializer,
                          VideoDetailSerializer, VideoListSerializer)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return VideoListSerializer
        return VideoDetailSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


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
