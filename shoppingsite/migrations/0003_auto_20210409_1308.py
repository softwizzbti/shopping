# Generated by Django 2.0 on 2021-04-09 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingsite', '0002_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='catid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='shoppingsite.category'),
        ),
    ]
