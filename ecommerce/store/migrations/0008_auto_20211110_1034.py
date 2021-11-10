# Generated by Django 3.2.7 on 2021-11-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='item',
            name='units',
            field=models.CharField(choices=[('KG', 'Kg'), ('GRAM', 'Gram'), ('NOS', 'Nos'), ('LITRE', 'Litre')], default='NOS', max_length=10),
        ),
    ]