from django.db import models
from django.template.defaultfilters import truncatechars

BOOK_STATUS_CHOICES = (
    ('available', 'Available'),
    ('checkedOut', 'Checked Out'),
    ('damaged', 'Damaged'),
    ('lost', 'Lost'),
    ('digitalCopy', 'Digital Copy')
)

BOOK_STATUS_DICT = {
    'available': 'Available',
    'checkedOut': 'Checked Out',
    'damaged': 'Damaged',
    'lost': 'Lost',
    'digitalCopy': 'Digital Copy'
}

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices=BOOK_STATUS_CHOICES, default="available", blank=True)
    statusBeforeCheckout = models.CharField(max_length=30, choices=BOOK_STATUS_CHOICES, default="available", blank=True)
    location = models.CharField(max_length=100)
    checkedOutBy = models.CharField(max_length=100, null=True, blank=True)
    checkOutDate= models.DateTimeField(null=True, blank=True)
    addedDate= models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=850)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_comments")
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)

    def __str__(self):
        return truncatechars(self.content, 15)

