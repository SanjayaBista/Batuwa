# Generated by Django 4.0.5 on 2022-07-01 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancing', '0008_remove_verificaion_address_delete_address'),
        ('UserAdmin', '0010_seosetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='seosetting',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer'),
        ),
    ]