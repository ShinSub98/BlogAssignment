from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'board'

urlpatterns =[
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/update/', BoardUpdate.as_view()),
    path('<int:pk>/destroy/', BoardDestroy.as_view()),
    path('<int:post>/comments/', CommentDetail.as_view()),
]

# app_name = 'board'

# urlpatterns = [
#     path('', BoardList.as_view()),
#     path('<int:pk>/', BoardDetail.as_view()),
#     path('comment/', views.comment_list), 
#     path('comment/<int:comment_pk>', views.comment_detail),
#     path('<int:comment_pk>/comments/', views.comment_create), 
# ]