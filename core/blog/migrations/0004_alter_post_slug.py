# Generated by Django 4.2.11 on 2024-05-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_banner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
