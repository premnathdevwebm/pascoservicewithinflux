# Generated by Django 4.2.6 on 2023-10-06 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labassets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="workflag",
            field=models.BooleanField(default=False),
        ),
    ]
