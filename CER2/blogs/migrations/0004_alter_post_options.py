# Generated by Django 4.2.2 on 2023-10-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_post_author_alter_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
    ]
