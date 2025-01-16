# viewSet vs ModelView

from rest_framework import viewsets

from .models import (About, Article, Comment, PrivacyPolicy, Question,
                     SocialMedia, TermsOfService, Video)
from .serializers import (AboutSerializer, ArticleSerializer,
                          CommentSerializer, PrivacyPolicySerializer,
                          QuestionSerializer, SocialMediaSerializer,
                          TermsOfServiceSerializer, VideoSerializer)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


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
