# Generated by Django 3.0.4 on 2020-04-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_feedback_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
