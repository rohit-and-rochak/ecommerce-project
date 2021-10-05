# Generated by Django 3.2.7 on 2021-10-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211005_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='items',
        ),
        migrations.AlterField(
            model_name='order',
            name='delievery',
            field=models.CharField(blank=True, choices=[('HOME DELIEVERY', 'Home Delievery'), ('PICKUP', 'Pickup')], default='HOME DELIEVERY', max_length=20),
        ),
    ]
