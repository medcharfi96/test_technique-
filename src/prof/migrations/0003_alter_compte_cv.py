# Generated by Django 3.2.9 on 2022-04-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_auto_20220402_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='CV',
            field=models.FileField(upload_to='prof'),
        ),
    ]