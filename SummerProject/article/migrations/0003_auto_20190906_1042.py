# Generated by Django 2.2.3 on 2019-09-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190823_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.URLField(max_length=150, null=True),
        ),
    ]