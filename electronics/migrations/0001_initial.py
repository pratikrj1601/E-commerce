# Generated by Django 3.1.7 on 2021-04-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cameras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('ram_size', models.CharField(max_length=10)),
                ('processor', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('ram_size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='speakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
