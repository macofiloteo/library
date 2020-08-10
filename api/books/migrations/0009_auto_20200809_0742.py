# Generated by Django 3.1 on 2020-08-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_addeddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('checkedOut', 'Checked Out'), ('damaged', 'Damaged'), ('lost', 'Lost'), ('digitalCopy', 'Digital Copy')], max_length=30),
        ),
    ]
