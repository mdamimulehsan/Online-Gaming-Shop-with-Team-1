# Generated by Django 3.1.7 on 2021-03-18 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Games.categories'),
        ),
    ]