# Generated by Django 4.1.6 on 2023-02-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_card_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('thirdname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('pas', models.CharField(max_length=20)),
            ],
        ),
    ]
