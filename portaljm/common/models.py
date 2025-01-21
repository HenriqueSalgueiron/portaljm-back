from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class TimeStampedModel(models.Model):
    created_at = AutoCreatedField(db_index=True, verbose_name='Criado em')
    updated_at = AutoLastModifiedField(
        db_index=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True


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
