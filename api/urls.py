from django.conf.urls import include
from api.books import views
from django.urls import path

urlpatterns = [
    path('books/', include('api.books.urls')),
]