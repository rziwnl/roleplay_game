# Generated by Django 5.0.6 on 2024-06-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('health', models.IntegerField(default=100)),
                ('experience', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=0)),
            ],
        ),
    ]
