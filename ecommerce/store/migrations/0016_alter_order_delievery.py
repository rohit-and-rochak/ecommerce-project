# Generated by Django 3.2.7 on 2021-12-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delievery',
            field=models.CharField(blank=True, choices=[('DELIEVERY', 'Delievery'), ('PICKUP', 'Pickup')], default='DELIEVERY', max_length=20),
        ),
    ]
