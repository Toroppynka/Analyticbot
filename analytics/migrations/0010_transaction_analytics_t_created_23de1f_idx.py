# Generated by Django 4.2.2 on 2023-07-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0009_transaction_gas_transaction_gas_price'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='transaction',
            index=models.Index(fields=['created_on'], name='analytics_t_created_23de1f_idx'),
        ),
    ]