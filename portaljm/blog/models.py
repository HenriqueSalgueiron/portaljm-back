from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models

from portaljm.common.models import TimeStampedModel


class Subject(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Assuntos'

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    content = RichTextField()
    reading_time = models.IntegerField(blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    banner_image = models.CharField(max_length=255, blank=True, null=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.title


class Video(TimeStampedModel):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    url = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Vídeos'

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    class Meta:
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.text


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return self.name


class About(TimeStampedModel):
    description = models.CharField(max_length=255)
    content = RichTextField()

    class Meta:
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return 'Sobre'


class PrivacyPolicy(TimeStampedModel):
    content = RichTextField()

    class Meta:
        verbose_name_plural = 'Política de privacidade'

    def __str__(self):
        return 'Política de privacidade'


class TermsOfService(TimeStampedModel):
    content = RichTextField()

    class Meta:
        verbose_name_plural = 'Termos de uso'

    def __str__(self):
        return 'Termos de uso'


class QuestionCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categorias de perguntas'

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=255)
    answer = RichTextField()
    category = models.ForeignKey(
        QuestionCategory, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.text
