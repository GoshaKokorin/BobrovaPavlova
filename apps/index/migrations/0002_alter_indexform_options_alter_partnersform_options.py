# Generated by Django 4.1 on 2022-10-07 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexform',
            options={'verbose_name': 'Форма обратной связи', 'verbose_name_plural': 'Форма обратной связи'},
        ),
        migrations.AlterModelOptions(
            name='partnersform',
            options={'verbose_name': 'Форма партнера', 'verbose_name_plural': 'Форма партнера'},
        ),
    ]