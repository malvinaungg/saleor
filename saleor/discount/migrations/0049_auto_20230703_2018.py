# Generated by Django 3.2.19 on 2023-07-03 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0025_auto_20230420_1544"),
        ("account", "0079_full_channel_access_group_for_openid"),
        ("discount", "0048_promotionevent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="promotionevent",
            name="app",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="app.app",
            ),
        ),
        migrations.AlterField(
            model_name="promotionevent",
            name="type",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="promotionevent",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="account.user",
            ),
        ),
    ]