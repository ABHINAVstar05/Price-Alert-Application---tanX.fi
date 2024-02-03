# Generated by Django 5.0.1 on 2024-02-03 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_purpose', models.CharField(max_length=500, unique=True)),
                ('alert_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('alert_status', models.CharField(choices=[('CREATED', 'Created'), ('DELETED', 'Deleted'), ('TRIGGERED', 'Triggered')], default='CREATED', max_length=20)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alert', to='alert_app.user')),
            ],
        ),
    ]