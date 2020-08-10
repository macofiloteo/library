from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class GenericListPostView(ListCreateAPIView):
    '''
        A generic view for /api/*model*/ URLS
        POST and GET ALL
    '''
    @classmethod
    def as_view(self, model=None, serializer_class=None, omit=None, **kwargs):
        self.model = model
        self.serializer_class = serializer_class
        self.omit = omit
        view = super(GenericListPostView, self).as_view(**kwargs)
        return view

    def get_queryset(self):
        models = self.model.objects.all()
        return models

    def get(self, request):
        model = self.get_queryset()
        serializer = self.serializer_class(model,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        for prop in self.omit['post']:
            if hasattr(data, prop):
                delattr(data, prop)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)



class GenericGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    '''
        A generic view for /api/*model*/*id* URLS
        GET id, UPDATE, DELETE
    '''

    @classmethod
    def as_view(self, model, serializer_class, **kwargs):
        self.model = model
        self.serializer_class = serializer_class
        view = super(GenericGetUpdateDeleteView, self).as_view(**kwargs)
        return view

    def get_queryset(self, pk):
        try:
            book = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return book

    def get(self, request, pk):
        book = self.get_queryset(pk)
        serializer = self.serializer_class(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request, pk):
        book = self.get_queryset(pk)
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self,request, pk):
        book = self.get_queryset(pk)
        book.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)