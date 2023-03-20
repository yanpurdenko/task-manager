# Generated by Django 4.1.4 on 2023-03-20 21:13

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_profile_is_uploaded_avatar_alter_profile_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="is_uploaded_avatar",
        ),
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="https://res.cloudinary.com/***REMOVED***/image/upload/v1679338671/media/default.png",
                upload_to=users.models.avatar_image_file_path,
            ),
        ),
    ]
