from rest_framework import serializers
from dataclasses import field
from .models import Board, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'created_at', 'comment']
        read_only_fields = ['user']

class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body', 'comments']
        read_only_fields = ['user']



# class BoardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Board
#         fields = ['id', 'user', 'title', 'body']
#         read_only_fields = ['user']

    
# class CommentSerializer(serializers.ModelSerializer) :
#     user = serializers.ReadOnlyField(source = 'user.nickname')
#     board = serializers.ReadOnlyField(source='board.id')
#     board = serializers.CharField(read_only=True)
#     class Meta :
#         model = Comment
#         fields = ['id', 'board', 'user', 'created_at', 'comment']