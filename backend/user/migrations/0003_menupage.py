# Generated by Django 2.2.7 on 2020-02-05 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200205_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
