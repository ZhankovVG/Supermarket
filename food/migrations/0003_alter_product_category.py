# Generated by Django 4.1.3 on 2023-03-26 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_rename_reting_rating_rename_retingsstar_ratingsstar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.category', verbose_name='Категория'),
        ),
    ]
