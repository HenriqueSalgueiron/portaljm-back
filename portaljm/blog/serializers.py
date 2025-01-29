from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import (About, Article, Comment, PrivacyPolicy, Question,
                     QuestionCategory, SocialMedia, Subject, TermsOfService,
                     Video)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class ArticleListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'cover_image', 'banner_image', 'subject']


class ArticleDetailSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class VideoListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'cover_image', 'subject']


class VideoDetailSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Video
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    content_type = serializers.CharField(write_only=True)
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'created_at', 'text', 'content_type', 'object_id', 'parent', 'children']
        read_only_fields = ['id', 'author_name', 'created_at', 'children']

    def get_children(self, obj):
        if obj.children.exists():
            return CommentSerializer(obj.children.all(), many=True).data
        return []

    def create(self, validated_data):
        content_type_str = validated_data.pop('content_type')
        content_type = ContentType.objects.get(model=content_type_str)
        validated_data['content_type'] = content_type
        return super().create(validated_data)

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'
        read_only_fields = ['name']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class TermsOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsOfService
        fields = '__all__'


class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = ['name']


class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Question
        fields = '__all__'
