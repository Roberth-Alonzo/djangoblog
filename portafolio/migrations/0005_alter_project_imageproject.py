# Generated by Django 5.0.6 on 2024-05-17 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portafolio", "0004_alter_project_imageproject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="imageProject",
            field=models.ImageField(
                null=True, upload_to="portafolio/portafolio_images/"
            ),
        ),
    ]
