# Generated by Django 3.1 on 2020-08-26 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]