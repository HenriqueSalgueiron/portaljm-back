from django.contrib import admin

from .models import (About, Article, Comment, PrivacyPolicy, Question,
                     QuestionCategory, SocialMedia, Subject, TermsOfService,
                     Video)

admin.site.register(About)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(PrivacyPolicy)
admin.site.register(Question)
admin.site.register(QuestionCategory)
admin.site.register(SocialMedia)
admin.site.register(Subject)
admin.site.register(TermsOfService)
admin.site.register(Video)
