# Generated by Django 4.2.11 on 2024-04-18 13:47

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
            name='GolfClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='golf_club_images/')),
                ('contact_information', models.CharField(max_length=200)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GolfersProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures/')),
                ('handicap', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('favorite_courses', models.ManyToManyField(blank=True, to='golfers_gateway.golfclub')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
