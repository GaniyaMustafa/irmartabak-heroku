# Generated by Django 2.2.10 on 2020-03-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20200321_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='martabak',
            name='selected',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], default='False', editable=False, max_length=50),
        ),
    ]
