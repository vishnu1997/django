# Generated by Django 2.0.3 on 2018-04-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproject',
            name='regno',
            field=models.DecimalField(decimal_places=0, max_digits=13),
        ),
    ]