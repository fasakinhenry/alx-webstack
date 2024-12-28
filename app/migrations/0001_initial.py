# Generated by Django 5.1.3 on 2024-12-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('profession', models.CharField(choices=[('Engineer', 'Engineer'), ('Doctor', 'Doctor'), ('Teacher', 'Teacher'), ('Lawyer', 'Lawyer'), ('Other', 'Other')], default='Other', max_length=50)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('CA', 'California'), ('NY', 'New York'), ('TX', 'Texas'), ('FL', 'Florida')], default='CA', max_length=50)),
            ],
        ),
    ]
