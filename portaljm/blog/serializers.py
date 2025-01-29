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
    author_name = serializers.CharField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'created_at', 'text', 'parent', 'children']

    def get_children(self, obj):
        if obj.children.exists():
            return CommentSerializer(obj.children.all(), many=True).data
        return []

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
