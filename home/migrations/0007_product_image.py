# Generated by Django 2.0.5 on 2018-05-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_image'),
        ),
    ]