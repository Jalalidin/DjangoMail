# Generated by Django 3.1.3 on 2021-04-12 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebMail', '0002_auto_20210411_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mails',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='users',
            name='mailAddress',
        ),
        migrations.AlterField(
            model_name='contacts',
            name='userNo',
            field=models.ForeignKey(db_column='userNo', on_delete=django.db.models.deletion.CASCADE, to='WebMail.users'),
        ),
    ]
