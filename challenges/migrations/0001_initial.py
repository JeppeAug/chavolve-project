# Generated by Django 3.0 on 2019-12-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('headline', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
