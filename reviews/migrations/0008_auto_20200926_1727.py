# Generated by Django 3.1.1 on 2020-09-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20200926_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
