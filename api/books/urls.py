from django.urls import include, path, re_path
from django.conf.urls import url
from . import views
from .models import Book, Comment
from .serializers import BookSerializer, CommentSerializer


urlpatterns = [
    path('', views.BookListCreate.as_view(),name='books_get_post'),
    path('<int:pk>/',views.BookDetail.as_view(),name='book_get_delete_update_details'),
    path('comments/<int:pk>/', views.CommentCreate.as_view(), name='comments_get_post'
    ),
    path('checkout/', views.CheckoutBook.as_view()),
    
]
