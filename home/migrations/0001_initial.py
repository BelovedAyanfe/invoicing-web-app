# Generated by Django 3.2.13 on 2022-05-24 11:54

from django.db import migrations, models
from django.db.models import Sum

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=60)),
                ('quantity', models.CharField(max_length=12)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]
