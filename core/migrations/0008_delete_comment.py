# Generated by Django 5.0 on 2024-01-01 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_comment_created_at_remove_comment_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]