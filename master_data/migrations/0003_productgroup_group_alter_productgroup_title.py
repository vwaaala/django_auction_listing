# Generated by Django 4.0 on 2021-12-13 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0002_alter_productgroup_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productgroup',
            name='group',
            field=models.CharField(default='machine', max_length=15),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='title',
            field=models.CharField(default='hi', max_length=100),
        ),
    ]
