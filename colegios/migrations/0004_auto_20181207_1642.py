# Generated by Django 2.1.4 on 2018-12-07 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegios', '0003_auto_20181207_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colegios',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_creation', to=settings.AUTH_USER_MODEL),
        ),
    ]