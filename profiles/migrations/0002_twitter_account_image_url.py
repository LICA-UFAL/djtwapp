# Generated by Django 2.1 on 2018-08-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter_account',
            name='image_url',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
