# Generated by Django 3.0.1 on 2024-01-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Sub', models.CharField(max_length=300)),
                ('Contact', models.BigIntegerField()),
            ],
        ),
    ]
