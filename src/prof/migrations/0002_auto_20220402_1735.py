# Generated by Django 3.2.9 on 2022-04-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv_text',
            name='owner',
        ),
        migrations.AlterField(
            model_name='compte',
            name='lettre_de_motivation',
            field=models.TextField(max_length=5, verbose_name='lettre_motivation'),
        ),
    ]