# Generated by Django 4.2.2 on 2023-07-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_coin_transaction_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
