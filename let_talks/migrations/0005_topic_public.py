# Generated by Django 3.2.5 on 2021-08-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('let_talks', '0004_auto_20210716_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='public',
            field=models.CharField(choices=[('1', 'Public'), ('2', 'Private')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
