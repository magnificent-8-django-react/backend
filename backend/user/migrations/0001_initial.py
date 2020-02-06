# Generated by Django 2.2.7 on 2020-02-05 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantTruck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('rating', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=3)),
                ('comment', models.TextField()),
                ('customer_voice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_voice', to='user.UserProfile')),
                ('truck_review', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_review', to='user.RestaurantTruck')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('restaurant_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_name', to='user.RestaurantTruck')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='user.RestaurantTruck')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.UserProfile')),
            ],
        ),
    ]
