# Generated by Django 3.2.1 on 2021-10-05 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kblock', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifuploads',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pdf_file', to=settings.AUTH_USER_MODEL),
        ),
    ]
