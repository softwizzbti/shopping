# Generated by Django 2.0 on 2021-03-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'subscribe',
            },
        ),
    ]
