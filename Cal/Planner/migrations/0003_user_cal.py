# Generated by Django 3.2.6 on 2023-05-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planner', '0002_auto_20230530_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cal',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]