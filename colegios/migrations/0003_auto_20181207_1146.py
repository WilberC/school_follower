# Generated by Django 2.1.4 on 2018-12-07 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegios', '0002_colegios_nombre_colegio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colegios',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_creation', to=settings.AUTH_USER_MODEL),
        ),
    ]
