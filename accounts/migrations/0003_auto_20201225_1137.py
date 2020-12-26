# Generated by Django 3.1.4 on 2020-12-25 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20201223_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followed_users',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]