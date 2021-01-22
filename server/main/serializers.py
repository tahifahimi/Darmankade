from rest_framework import serializers

from authentication.serializers import UserSerializer
from main.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super(CommentSerializer, self).create(validated_data)
