from rest_framework import serializers
from dataclasses import field
from .models import Board, Comment

class BoardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Board
        fields = ['id', 'title', 'date', 'user', 'body']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'board', 'user', 'created_at', 'comment']




##### v1
# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source = 'user.nickname')
#     class Meta:
#         model = Comment
#         fields = ['id', 'post', 'user', 'created_at', 'comment']

# class BoardSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)
#     class Meta:
#         model = Board
#         fields = ['id', 'user', 'title', 'body', 'comments']

