# Generated by Django 2.2 on 2019-06-24 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('tabstructure', '0003_auto_20190624_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('main_title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Main Page',
                'verbose_name_plural': 'Main Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
