# from django.core.exceptions import ValidationError
from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class BaseModel(models.Model):
    created_at = AutoCreatedField(db_index=True, verbose_name='Criado em')
    updated_at = AutoLastModifiedField(
        db_index=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True


# class SingletonModel(models.Model):
#     class Meta:
#         abstract = True

#     def save(self, *args, **kwargs):
#         if not self.pk and self.__class__.objects.exists():
#             raise ValidationError(
#                 f"Only one {self.__class__.__name__} instance is allowed.")
#         return super().save(*args, **kwargs)
