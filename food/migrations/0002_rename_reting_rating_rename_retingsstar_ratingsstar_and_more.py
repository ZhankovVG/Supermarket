# Generated by Django 4.1.3 on 2023-03-24 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reting',
            new_name='Rating',
        ),
        migrations.RenameModel(
            old_name='RetingsStar',
            new_name='RatingsStar',
        ),
        migrations.AlterModelOptions(
            name='ratingsstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]