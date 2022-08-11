# Generated by Django 4.0.6 on 2022-08-11 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
