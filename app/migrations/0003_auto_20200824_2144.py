# Generated by Django 3.0.8 on 2020-08-24 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_program_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programversions',
            name='program',
            field=models.ForeignKey(default='2ab111e8-57d8-4086-a8ed-dbf23897d71f', on_delete=django.db.models.deletion.CASCADE, to='app.Program'),
            preserve_default=False,
        ),
    ]
