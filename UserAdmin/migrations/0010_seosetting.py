# Generated by Django 4.0.5 on 2022-07-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAdmin', '0009_paypalpayment_user_stripepayment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('keyword', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]
