# Generated by Django 4.1.4 on 2022-12-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lukafuluapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decharges',
            name='photo_decharge',
            field=models.ImageField(default=None, upload_to='pictures'),
        ),
    ]
