# Generated by Django 4.0.5 on 2022-06-24 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancing', '0008_remove_verificaion_address_delete_address'),
        ('UserAdmin', '0003_alter_website_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer'),
        ),
    ]