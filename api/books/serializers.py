from rest_framework import serializers
from .models import Book, Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    book_comments = CommentSerializer(many=True, read_only=True)
    status = serializers.CharField(required=False)
    checkOutBy = serializers.CharField(required=False)
    checkOutDate = serializers.DateTimeField(required=False, allow_null=True)
    addedDate = serializers.DateTimeField(required=False)
    class Meta:
        model = Book
        exclude = ['statusBeforeCheckout']