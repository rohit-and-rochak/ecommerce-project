# Generated by Django 3.2.7 on 2021-10-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20211005_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='store.Item'),
        ),
    ]
