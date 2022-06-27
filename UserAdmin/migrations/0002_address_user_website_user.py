# Generated by Django 4.0.5 on 2022-06-24 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancing', '0008_remove_verificaion_address_delete_address'),
        ('UserAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer'),
        ),
        migrations.AddField(
            model_name='website',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer'),
        ),
    ]
