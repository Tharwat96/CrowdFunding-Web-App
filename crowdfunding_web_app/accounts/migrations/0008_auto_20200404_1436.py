# Generated by Django 3.0.4 on 2020-04-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200403_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/jo.jpg', upload_to='profile_pic'),
        ),
    ]
