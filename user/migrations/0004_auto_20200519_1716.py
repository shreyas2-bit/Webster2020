# Generated by Django 3.0.3 on 2020-05-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tag', '0001_initial'),
        ('user', '0003_profile_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='user_tags', to='Tag.Tag'),
        ),
    ]
