# Generated by Django 2.2 on 2019-06-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabstructure', '0006_python'),
    ]

    operations = [
        migrations.AddField(
            model_name='ios',
            name='ios_subtitle',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
