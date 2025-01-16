from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AboutViewSet, ArticleViewSet, CommentViewSet,
                    PrivacyPolicyViewSet, QuestionViewSet, SocialMediaViewSet,
                    TermsOfServiceViewSet, VideoViewSet)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'social-media', SocialMediaViewSet)
router.register(r'about', AboutViewSet)
router.register(r'privacy-policy', PrivacyPolicyViewSet)
router.register(r'terms-of-service', TermsOfServiceViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
