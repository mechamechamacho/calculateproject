# Generated by Django 3.2.3 on 2021-06-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WarikanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField()),
                ('anum', models.IntegerField()),
                ('bnum', models.IntegerField()),
                ('cnum', models.IntegerField()),
                ('diffab', models.IntegerField()),
                ('diffac', models.IntegerField()),
                ('postdate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]