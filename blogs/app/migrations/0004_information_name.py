# Generated by Django 3.2.9 on 2022-11-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='name',
            field=models.CharField(default='獜洛橙', max_length=20),
        ),
    ]
