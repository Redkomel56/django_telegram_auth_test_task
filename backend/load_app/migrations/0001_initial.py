# Generated by Django 5.1.4 on 2024-12-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('auth_uuid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tg_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
