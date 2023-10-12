# Generated by Django 4.2.6 on 2023-10-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0002_category_slides_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='groups',
            field=models.ManyToManyField(related_name='custom_user_set', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customeuser',
            name='user_permissions',
            field=models.ManyToManyField(related_name='custom_user_set', to='auth.permission'),
        ),
    ]