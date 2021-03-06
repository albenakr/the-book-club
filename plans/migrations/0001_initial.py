# Generated by Django 3.1.1 on 2020-10-02 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=454)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('plan_duration', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('books', models.ManyToManyField(to='products.Book')),
            ],
        ),
    ]
