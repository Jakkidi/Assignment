# Generated by Django 4.1.1 on 2022-09-30 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('size', models.CharField(max_length=100)),
                ('quality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateField()),
                ('producttitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.product')),
            ],
        ),
    ]
