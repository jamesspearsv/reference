# Generated by Django 4.2 on 2023-04-16 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='location',
            field=models.CharField(choices=[('circulation', 'Circulation'), ('reference', 'Reference'), ('childrens', 'Childrens')], max_length=64),
        ),
    ]
