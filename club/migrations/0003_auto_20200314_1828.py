# Generated by Django 3.0.3 on 2020-03-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20200314_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete',
            name='card_type',
            field=models.CharField(choices=[('trending_posts', 'LATEST_POSTS'), ('events', 'EVENTS'), ('coupons', 'COUPONS'), ('category', 'CATEGORY'), ('most_popular', 'MOST_POPULAR')], default='trending_posts', max_length=100),
        ),
        migrations.AddField(
            model_name='complete',
            name='image_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]