# Generated by Django 3.2.7 on 2021-10-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='items'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('DAIRY', 'Dairy'), ('FRUITS', 'Fruits'), ('DAILY NEEDS', 'Daily Needs'), ('GENERIC', 'Generic')], default='GENERIC', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='delievery',
            field=models.CharField(blank=True, choices=[('HOME_DELIEVERY', 'Home Delievery'), ('PICKUP', 'Pickup')], default='HOME_DELIEVERY', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('PLACED', 'Placed'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, choices=[('CANCELLED', 'Cancelled'), ('FAILED', 'Failed'), ('PENDING', 'Pending'), ('SUCCESSFULL', 'Successfull')], default='PENDING', max_length=20),
        ),
    ]
