# Generated by Django 3.2.9 on 2022-04-03 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_alter_compte_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='lettre_de_motivation',
            field=models.TextField(max_length=500, verbose_name='lettre_motivation'),
        ),
    ]