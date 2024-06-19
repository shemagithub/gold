# Generated by Django 5.0.4 on 2024-05-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_products_prodapp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('name', models.TextField(default='')),
                ('blog_image', models.ImageField(upload_to='product')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]