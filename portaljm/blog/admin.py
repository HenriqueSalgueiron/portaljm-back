
from django.contrib import admin

from portaljm.common.models import SingletonModelAdmin

from .models import (About, Article, Carousel, Comment, PrivacyPolicy,
                     Question, QuestionCategory, SocialMedia, Subject,
                     TermsOfService, Video)

admin.site.register(About, SingletonModelAdmin)
admin.site.register(TermsOfService, SingletonModelAdmin)
admin.site.register(PrivacyPolicy, SingletonModelAdmin)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(QuestionCategory)
admin.site.register(SocialMedia)
admin.site.register(Subject)
admin.site.register(Video)
admin.site.register(Carousel)
