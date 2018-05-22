from rest_framework import serializers
from .models.snippet import Snippet
from .models import Circle
 

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.CharField(default='python')
    style = serializers.CharField( default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class CircleSerializer(serializers.ModelSerializer):
    story_title = serializers.SerializerMethodField()
    story_id = serializers.SerializerMethodField()
    age_group = serializers.SerializerMethodField()

    class Meta:
        model = Circle
        exclude = ('story',)
        
    def get_story_title(self, instance):
        return instance.story.story_title

    def get_story_id(self, instance):
        return instance.story.story_id
    
    def get_age_group(self, instance):
        return instance.story.age_group