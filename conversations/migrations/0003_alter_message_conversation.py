# Generated by Django 4.2.5 on 2023-09-22 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("conversations", "0002_alter_message_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="conversation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="conversations.conversation",
            ),
        ),
    ]