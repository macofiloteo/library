from django.urls import include, path, re_path
from api.views import GenericListPostView, GenericGetUpdateDeleteView
from . import views
from .models import Book, Comment
from .serializers import BookSerializer, CommentSerializer


urlpatterns = [
    path('comments/', 
        GenericListPostView.as_view(model=Comment, serializer_class=CommentSerializer, omit={'post': ['timestamp']}),
        name='comments_get_post'
    ),
    path('checkout/', views.CheckoutBook.as_view()),
    path('<int:pk>/', # Url to get update or delete a movie
        GenericGetUpdateDeleteView.as_view(model=Book, serializer_class=BookSerializer),
        name='book_get_delete_update_details'
    ),

    path('', GenericListPostView.as_view(model=Book, serializer_class=BookSerializer, omit={'post': ['status', 'checkedOutBy', 'checkOutDate', 'addedDate']}),
    name='books_get_post'),
    
]
