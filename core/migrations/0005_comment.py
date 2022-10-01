# Generated by Django 4.1.1 on 2022-09-30 12:53

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followerscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('commment', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
