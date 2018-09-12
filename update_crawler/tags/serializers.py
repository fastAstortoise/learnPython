from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tags, ProgrammingLanguage


class TagsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tags
        fields = ('id', 'tag_name', 'owner', 'created_on', 'tag_code', 'created_by')


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgrammingLanguage
        fields = ('id', 'code', 'description')


class UserSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tags.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tags')
