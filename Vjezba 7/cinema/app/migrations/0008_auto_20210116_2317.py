# Generated by Django 3.1.5 on 2021-01-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_projection_userticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seatNumber',
            field=models.IntegerField(null=True),
        ),
    ]
