from rest_framework import serializers
from rabble.models import Subrabbles, Posts
from django.contrib.auth import get_user_model

User = get_user_model()
class SubrabblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subrabbles
        fields = ['id', 'identifier', 'subrabble_name', 'description', 'is_public', 'num_posts', 'num_comments', 'allow_anon']

class PostsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', source='user', queryset=User.objects.all())
    subrabble = serializers.SlugRelatedField(slug_field='identifier', read_only=True)  

    class Meta:
        model = Posts
        fields = ['id', 'title', 'body', 'author', 'subrabble']
