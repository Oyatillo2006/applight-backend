# Generated by Django 4.2.5 on 2023-09-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='text',
        ),
        migrations.AddField(
            model_name='test',
            name='image',
            field=models.ImageField(default=12, upload_to='images/test/'),
            preserve_default=False,
        ),
    ]
