# Generated by Django 2.1.2 on 2018-11-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181102_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]