# Generated by Django 5.1.6 on 2025-02-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='course_previews/'),
        ),
    ]
