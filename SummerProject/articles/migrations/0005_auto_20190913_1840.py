# Generated by Django 2.2.3 on 2019-09-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190912_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(to='articles.Comment'),
        ),
    ]
