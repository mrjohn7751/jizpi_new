# Generated by Django 5.0.7 on 2024-07-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleelon',
            name='created_at',
            field=models.CharField(max_length=10, verbose_name='Sana kiritish'),
        ),
        migrations.AlterField(
            model_name='articlenews',
            name='created_at',
            field=models.CharField(max_length=10, verbose_name='Sana kiritish'),
        ),
    ]