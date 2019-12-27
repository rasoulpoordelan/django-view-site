# Generated by Django 3.0.1 on 2019-12-27 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_num', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('props', models.ManyToManyField(to='api.Prop')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TrainInfo')),
            ],
        ),
    ]
