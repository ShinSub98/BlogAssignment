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
class BoardList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        board = get_object_or_404(Board, pk=pk)
        return board

    def get(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def put(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)







#### v1 
# class BoardList(ListCreateAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     authentication_classes = [BasicAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user = user)


# class BoardDetail(RetrieveAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer

# class BoardUpdate(UpdateAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     authentication_classes = [BasicAuthentication, SessionAuthentication]
#     permission_classes = [IsOwnerOrReadOnly]

# class BoardDestroy(DestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     authentication_classes = [BasicAuthentication, SessionAuthentication]
#     permission_classes = [IsOwnerOrReadOnly]
# 
# class CommentDetail(ListAPIView, CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def get_queryset(self):
#         post_id = self.kwargs['post']
#         return Comment.objects.filter(post=post_id)

#     authentication_classes = [BasicAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user = user)
