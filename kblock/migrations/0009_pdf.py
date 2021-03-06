# Generated by Django 3.1.13 on 2021-10-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kblock', '0008_delete_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
