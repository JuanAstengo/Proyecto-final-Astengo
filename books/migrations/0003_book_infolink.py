# Generated by Django 5.0.6 on 2024-06-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_cover_book_pdf_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='infoLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]
