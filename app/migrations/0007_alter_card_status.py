# Generated by Django 4.1.5 on 2023-02-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_card_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('Дебетовая', 'Дебетовая'), ('Кредитная', 'Кредитная')], max_length=35),
        ),
    ]
