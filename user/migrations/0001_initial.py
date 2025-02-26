# Generated by Django 3.0.3 on 2020-11-01 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moderator', models.BooleanField(default=False)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.TextField(blank=True, default=' ')),
                ('country', models.CharField(blank=True, default=' ', max_length=50)),
                ('gender', models.IntegerField(choices=[(0, 'Not Defined'), (1, 'Male'), (2, 'Female')], default=0)),
                ('currency', models.IntegerField(default=0)),
                ('notif', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('followings', models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='user_tags', to='Tag.Tag')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
