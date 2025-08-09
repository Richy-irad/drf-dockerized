from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):

    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes and deserializes Snippet instances, mapping model fields to their
    corresponding serializer fields for use in API representations.


    Meta:
        model: Snippet
        fields: ['id', 'title', 'code', 'linenos', 'language', 'style']


    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos',
                  'language', 'style', 'owner', 'highlight']
