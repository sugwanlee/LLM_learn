# Generated by Django 4.2 on 2025-01-24 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chatbot",
            old_name="bot_massage",
            new_name="bot_message",
        ),
        migrations.RenameField(
            model_name="chatbot",
            old_name="user_massage",
            new_name="user_message",
        ),
    ]
