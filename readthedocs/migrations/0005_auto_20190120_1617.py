# Generated by Django 2.1.5 on 2019-01-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readthedocs', '0004_scraperesult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraperesult',
            name='folder',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
