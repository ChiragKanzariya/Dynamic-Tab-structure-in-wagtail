# Generated by Django 2.2 on 2019-06-25 06:50

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tabstructure', '0012_auto_20190625_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='ios',
            name='ios_extra_detail',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nodejs',
            name='nodejs_content_detail',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='nodejs',
            name='nodejs_extra_detail',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='python',
            name='python_content_detail',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='python',
            name='python_extra_detail',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
