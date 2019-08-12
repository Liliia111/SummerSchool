# Generated by Django 2.2.3 on 2019-08-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
