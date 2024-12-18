from django.db import migrations, models
import json

def clean_completed_lessons(apps, schema_editor):
    """
    Safely migrate completed_lessons field data to JSONField.
    """
    UserProgress = apps.get_model("progress", "UserProgress")
    for progress in UserProgress.objects.all():
        try:
            # If the current value is an integer, wrap it in a list
            if isinstance(progress.completed_lessons, int):
                progress.completed_lessons = json.dumps([progress.completed_lessons])
            # If the current value is a string, load it safely
            elif isinstance(progress.completed_lessons, str):
                # Validate if the string is already a JSON list
                try:
                    loaded_value = json.loads(progress.completed_lessons)
                    if isinstance(loaded_value, list):
                        progress.completed_lessons = json.dumps(loaded_value)
                    else:
                        progress.completed_lessons = json.dumps([])
                except json.JSONDecodeError:
                    progress.completed_lessons = json.dumps([])
            else:
                # Default case if no valid type is found
                progress.completed_lessons = json.dumps([])
        except Exception as e:
            # Fallback in case of unexpected issues
            progress.completed_lessons = json.dumps([])
        progress.save()

class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0002_initial'),  # Replace with the correct previous migration
    ]

    operations = [
        # Add a temporary field
        migrations.AddField(
            model_name='userprogress',
            name='completed_lessons_temp',
            field=models.JSONField(default=list),
        ),
        # Clean data and migrate to the temporary field
        migrations.RunPython(clean_completed_lessons),
        # Remove the old field
        migrations.RemoveField(
            model_name='userprogress',
            name='completed_lessons',
        ),
        # Rename the temporary field to completed_lessons
        migrations.RenameField(
            model_name='userprogress',
            old_name='completed_lessons_temp',
            new_name='completed_lessons',
        ),
    ]
