# Generated by Django 5.1.2 on 2024-11-06 15:18

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_category_post_categories_comment"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="post",
            managers=[
                ("custom_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="post_images/"),
        ),
    ]
