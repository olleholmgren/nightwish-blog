# Generated by Django 3.2.19 on 2023-06-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nw_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=0),
        ),
    ]