# Generated by Django 3.1.2 on 2020-10-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='username')),
                ('password', models.CharField(max_length=64, verbose_name='password')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='time')),
            ],
            options={
                'db_table': 'basic_user1',
            },
        ),
    ]
