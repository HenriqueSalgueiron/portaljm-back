import django_filters

from .models import Article, Video


class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    subject = django_filters.NumberFilter(field_name='subject__id')

    class Meta:
        model = Article
        fields = ['title', 'subject']


class VideoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    subject = django_filters.NumberFilter(field_name='subject__id')

    class Meta:
        model = Video
        fields = ['title', 'subject']
