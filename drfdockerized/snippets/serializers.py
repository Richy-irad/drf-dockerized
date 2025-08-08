from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializes and deserializes Snippet instances, mapping model fields to their
    corresponding serializer fields for use in API representations.


    Meta:
        model: Snippet
        fields: ['id', 'title', 'code', 'linenos', 'language', 'style']


    """
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
