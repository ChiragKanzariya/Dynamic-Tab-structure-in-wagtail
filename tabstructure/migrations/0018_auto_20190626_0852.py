# Generated by Django 2.2 on 2019-06-26 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabstructure', '0017_auto_20190625_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainindexpage',
            name='subpage_subtitle',
        ),
        migrations.RemoveField(
            model_name='mainindexpage',
            name='subpage_title',
        ),
    ]
