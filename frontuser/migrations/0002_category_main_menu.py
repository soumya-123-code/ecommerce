# Generated by Django 2.0.6 on 2018-06-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_menu',
            field=models.CharField(choices=[('mt', 'Men-TShirt'), ('sh', 'Shoes'), ('mb', 'Mobile')], default='sh', max_length=2),
            preserve_default=False,
        ),
    ]
