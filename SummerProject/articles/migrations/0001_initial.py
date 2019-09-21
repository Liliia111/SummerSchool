# Generated by Django 2.2.3 on 2019-09-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=150)),
                ('photo', models.URLField(max_length=150)),
                ('video', models.URLField(max_length=150)),
                ('source', models.CharField(choices=[('GG', 'google'), ('FB', 'facebook'), ('TW', 'twitter')], max_length=2)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]