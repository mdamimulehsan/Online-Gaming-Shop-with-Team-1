# Generated by Django 3.1.6 on 2021-03-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='+880', max_length=12)),
                ('password', models.CharField(max_length=500)),
                ('re_password', models.CharField(max_length=500)),
            ],
        ),
    ]