# Generated by Django 3.0 on 2019-12-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191221_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeaction',
            name='user_name',
            field=models.CharField(blank=True, default='No one', max_length=50),
        ),
    ]