# Generated by Django 3.1.7 on 2021-03-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_auto_20210318_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]