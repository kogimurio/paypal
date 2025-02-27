# Generated by Django 4.2.10 on 2024-02-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
