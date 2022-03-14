# Generated by Django 3.2.4 on 2022-02-21 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(max_length=100)),
                ('temp', models.FloatField(max_length=200)),
                ('cough', models.IntegerField(max_length=10)),
                ('sore_throat', models.IntegerField(max_length=10)),
                ('breathing', models.IntegerField(max_length=10)),
                ('headache', models.IntegerField(max_length=10)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]
