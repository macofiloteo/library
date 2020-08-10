# Generated by Django 3.1 on 2020-08-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20200809_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='statusBeforeCheckout',
            field=models.CharField(blank=True, choices=[('available', 'Available'), ('checkedOut', 'Checked Out'), ('damaged', 'Damaged'), ('lost', 'Lost'), ('digitalCopy', 'Digital Copy')], default='available', max_length=30),
        ),
    ]
