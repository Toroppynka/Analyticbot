# Generated by Django 4.2.2 on 2023-07-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Sell', 'Sell')], max_length=10),
        ),
    ]
