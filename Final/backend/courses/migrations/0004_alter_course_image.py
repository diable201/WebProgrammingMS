# Generated by Django 5.1.2 on 2024-12-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0003_course_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="image",
            field=models.CharField(
                help_text="Upload the course image.", verbose_name="Course Image"
            ),
        ),
    ]