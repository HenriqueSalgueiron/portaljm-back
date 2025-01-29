import django_filters
from django.contrib.contenttypes.models import ContentType

from .models import Article, Comment, Video


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


class CommentFilter(django_filters.FilterSet):
    content_type = django_filters.CharFilter(method='filter_by_content_type')
    object_id = django_filters.NumberFilter(field_name='object_id')

    class Meta:
        model = Comment
        fields = ['content_type', 'object_id']

    def filter_by_content_type(self, queryset, name, value):
        content_type = ContentType.objects.get(model=value)
        return queryset.filter(content_type=content_type)
