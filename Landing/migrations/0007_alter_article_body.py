# Generated by Django 3.2.9 on 2022-06-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing', '0006_alter_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.CharField(max_length=5000),
        ),
    ]