# Generated by Django 3.2.12 on 2023-02-18 18:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification Date and Time')),
                ('name', models.CharField(max_length=200)),
                ('members', models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
