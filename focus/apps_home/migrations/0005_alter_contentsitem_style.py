# Generated by Django 4.0.4 on 2022-05-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0004_rename_color_contentsitem_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentsitem',
            name='style',
            field=models.CharField(default='', max_length=50),
        ),
    ]
