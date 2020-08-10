from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.views import APIView
from .models import Book, BOOK_STATUS_DICT
from django.forms.models import model_to_dict

class CheckoutBook(APIView):

    def get_queryset(self, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return book

    def post(self, request, format=None):
        data = request.data
        book = self.get_queryset(data['id'])
        if data['willReturn']:
            book.checkOutDate = None
            book.checkedOutBy = None 
            book.status = book.statusBeforeCheckout
        else:
            book.checkOutDate = datetime.now().isoformat()
            book.checkedOutBy = data['checkedOutBy']
            book.statusBeforeCheckout = book.status
            book.status = "Checked Out"
        serializer = BookSerializer(book,data=model_to_dict(book), allow_null=True)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
