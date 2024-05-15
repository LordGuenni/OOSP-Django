# Generated by Django 5.0.6 on 2024-05-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subnets', '0003_rename_ipadress_subnetgen_ipadresswithcdir'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('device_type', models.CharField(choices=[('MOBILE', 'Mobile'), ('DESKTOP', 'Desktop')], default='DESKTOP', max_length=7)),
                ('subnets', models.ManyToManyField(to='subnets.subnetgen')),
            ],
        ),
    ]