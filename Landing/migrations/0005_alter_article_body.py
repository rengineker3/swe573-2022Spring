# Generated by Django 3.2.9 on 2022-06-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing', '0004_alter_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.CharField(max_length=5000),
        ),
    ]
