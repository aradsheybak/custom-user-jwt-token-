# Generated by Django 4.2.4 on 2023-09-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_customuser_birthday_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
    ]
