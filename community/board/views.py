from django.shortcuts import render
from .models import Board, Comment
from .serializers import BoardSerializer, CommentSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from . import serializers

# Create your views here.
class BoardList(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)


class BoardDetail(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardUpdate(UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

class BoardDestroy(DestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

#============================================================================
class CommentDetail(ListAPIView, CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post']
        return Comment.objects.filter(post=post_id)

    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)


# class BoardDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     authentication_classes = [BasicAuthentication, SessionAuthentication]


# @api_view(['GET'])
# def comment_list(request) :
#     comments = get_list_or_404(Comment)
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def comment_detail(request, comment_pk) :
#     comments = get_list_or_404(Comment, pk = comment_pk)
#     serializer = CommentSerializer(comments)
#     return Response(serializer.data)


# @api_view(['POST'])
# def comment_create(request, board_pk) :
#     board = get_list_or_404(Board, pk = board_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True) :
#         serializer.save(board=board) # 해당 글에 댓글쓰기
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'DELETE'])
# def comment_detail(request, comment_pk) :
#     comment = get_list_or_404(Comment, pk = comment_pk)
#     if request.method == 'GET' :
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
#     elif request.method == "DELETE" :
#         comment.delete()
#         data= {
#             'delete' :f'댓글 {comment_pk}번이 삭제 되었습니다.'
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'DELETE', 'PUT'])
# def comment_detail(request, comment_pk) :
#     comment = get_list_or_404(Comment, pk = comment_pk)
#     if request.method == 'GET' :
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
#     elif request.method == "DELETE" :
#         comment.delete()
#         data= {
#             'delete' :f'댓글 {comment_pk}번이 삭제 되었습니다.'
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PUT" :
#         serializer = CommentSerializer(instance=comment, data=request.data)
#         if serializer.is_valid(raise_exception=True) :
#             serializer.save()
#             return Response(serializer.data)
