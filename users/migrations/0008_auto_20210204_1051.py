# Generated by Django 3.1.5 on 2021-02-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210203_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialuser',
            name='birthdate',
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
