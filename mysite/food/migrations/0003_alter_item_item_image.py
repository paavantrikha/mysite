# Generated by Django 4.1.4 on 2023-06-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='http://www.ukvisitorguide.cn/wp-content/uploads/2015/11/Food-placeholder.jpg', max_length=500),
        ),
    ]
