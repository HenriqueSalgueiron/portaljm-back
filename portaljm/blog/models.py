from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models

from portaljm.common.models import TimeStampedModel


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')

    class Meta:
        verbose_name_plural = 'Assuntos'
        verbose_name = 'Assunto'

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    title = models.CharField(max_length=60, verbose_name='Título')
    description = models.CharField(max_length=650, verbose_name='Descrição')
    content = RichTextField(verbose_name='Conteúdo')
    reading_time = models.IntegerField(blank=True, null=True, help_text="Tempo de leitura em minutos", verbose_name='Tempo de leitura')
    cover_image = models.CharField(max_length=255, blank=True, null=True, help_text="Dimensões recomendadas: 468x272px", verbose_name='Imagem de capa')
    banner_image = models.CharField(max_length=255, blank=True, null=True, help_text="Dimensões recomendadas: 2160x740px", verbose_name='Imagem do banner')
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Assunto')

    class Meta:
        verbose_name_plural = 'Artigos'
        verbose_name = 'Artigo'

    def __str__(self):
        return self.title


class Video(TimeStampedModel):
    title = models.CharField(max_length=60, verbose_name='Título')
    description = models.CharField(max_length=650, verbose_name='Descrição')
    url = models.CharField(max_length=255, verbose_name='Link do youtube')
    cover_image = models.CharField(max_length=255, blank=True, null=True, help_text="Dimensões recomendadas: 468x272px", verbose_name='Imagem de capa')
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Assunto')

    class Meta:
        verbose_name_plural = 'Vídeos'
        verbose_name = 'Vídeo'

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    text = models.CharField(max_length=255, verbose_name='Texto')
    post = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Artigo')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Autor')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Comentário pai'
    )

    class Meta:
        verbose_name_plural = 'Comentários'
        verbose_name = 'Comentário'

    def __str__(self):
        return self.text


class SocialMedia(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    url = models.CharField(max_length=255, blank=True, verbose_name='URL')

    class Meta:
        verbose_name_plural = 'Redes Sociais'
        verbose_name = 'Rede Social'

    def __str__(self):
        return self.name


class About(TimeStampedModel):
    description = models.CharField(max_length=255, verbose_name='Descrição')
    content = RichTextField(verbose_name='Conteúdo')

    class Meta:
        verbose_name_plural = 'Sobre'
        verbose_name = 'Sobre'

    def __str__(self):
        return 'Sobre'


class PrivacyPolicy(TimeStampedModel):
    content = RichTextField(verbose_name='Conteúdo')

    class Meta:
        verbose_name_plural = 'Política de Privacidade'
        verbose_name = 'Política de Privacidade'

    def __str__(self):
        return 'Política de Privacidade'


class TermsOfService(TimeStampedModel):
    content = RichTextField(verbose_name='Conteúdo')

    class Meta:
        verbose_name_plural = 'Termos de Uso'
        verbose_name = 'Termos de Uso'

    def __str__(self):
        return 'Termos de Uso'


class QuestionCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')

    class Meta:
        verbose_name_plural = 'Categorias de Pergunta'
        verbose_name = 'Categoria de Pergunta'

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='Texto')
    answer = RichTextField(verbose_name='Resposta')
    category = models.ForeignKey(
        QuestionCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')

    class Meta:
        verbose_name_plural = 'Perguntas'
        verbose_name = 'Pergunta'

    def __str__(self):
        return self.text
