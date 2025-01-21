from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError

from .models import (About, Article, Comment, PrivacyPolicy, Question,
                     QuestionCategory, SocialMedia, Subject, TermsOfService,
                     User, Video)


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('country', 'phone')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('country', 'phone')}),
    )


class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def save_model(self, request, obj, form, change):
        if not change and self.model.objects.exists():
            raise ValidationError(
                f'Only one instance of {self.model.__name__} is allowed.')
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
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
