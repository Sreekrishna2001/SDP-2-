# Generated by Django 3.2 on 2021-05-17 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0009_alter_uprofile_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='tablebooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tableno', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orderfood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preffood', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
