# Generated by Django 2.1 on 2018-09-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20180925_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='paginas',
            field=models.IntegerField(default=100),
        ),
    ]
