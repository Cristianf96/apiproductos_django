# Generated by Django 3.2.9 on 2021-11-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('paused', models.BooleanField()),
                ('images', models.URLField()),
            ],
        ),
    ]
