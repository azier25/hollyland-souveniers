# Generated by Django 2.2.4 on 2020-12-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollylandApp', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]
