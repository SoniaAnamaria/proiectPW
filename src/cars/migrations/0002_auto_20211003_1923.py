# Generated by Django 3.2.7 on 2021-10-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='tyre_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(default='green', max_length=50),
        ),
    ]