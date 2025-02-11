from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AboutViewSet, ArticleViewSet, CarouselViewSet,
                    CommentViewSet, PrivacyPolicyViewSet, QuestionViewSet,
                    SocialMediaViewSet, SubjectViewSet, TermsOfServiceViewSet,
                    VideoViewSet)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'social-media', SocialMediaViewSet)
router.register(r'about', AboutViewSet)
router.register(r'privacy-policy', PrivacyPolicyViewSet)
router.register(r'terms-of-service', TermsOfServiceViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'carousel', CarouselViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
