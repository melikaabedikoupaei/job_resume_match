# Generated by Django 5.1.1 on 2024-09-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0002_resume"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resume",
            old_name="pdf_file",
            new_name="resume_file",
        ),
        migrations.AddField(
            model_name="resume",
            name="resume_content",
            field=models.TextField(blank=True, null=True),
        ),
    ]
