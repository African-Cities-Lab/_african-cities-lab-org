# Generated by Django 3.1.13 on 2022-09-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220912_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='language',
            field=models.TextField(choices=[('english', 'English'), ('french', 'French')], default='english', max_length=10),
        ),
    ]