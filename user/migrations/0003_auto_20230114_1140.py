# Generated by Django 3.2.14 on 2023-01-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_group_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='cat',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='star',
            field=models.IntegerField(default=0),
        ),
    ]
