# Generated by Django 4.1.1 on 2022-09-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='address',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
