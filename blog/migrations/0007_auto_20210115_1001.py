# Generated by Django 3.1.1 on 2021-01-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210115_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeimage',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
