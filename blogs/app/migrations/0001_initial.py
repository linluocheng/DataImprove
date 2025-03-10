# Generated by Django 4.1 on 2022-09-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('bid', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField(null=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('avatar', models.CharField(default='default.jpg', max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
