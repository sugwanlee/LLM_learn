# Generated by Django 4.2 on 2025-01-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0002_rename_bot_massage_chatbot_bot_message_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatbot",
            name="created_at",
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="chatbot",
            name="updated_at",
            field=models.TimeField(auto_now=True),
        ),
    ]
