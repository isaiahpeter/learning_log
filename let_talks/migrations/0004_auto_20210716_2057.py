# Generated by Django 3.2.5 on 2021-07-16 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('let_talks', '0003_topic_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]