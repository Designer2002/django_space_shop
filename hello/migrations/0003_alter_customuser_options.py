# Generated by Django 5.1.4 on 2024-12-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
