# Generated by Django 3.0.8 on 2020-08-24 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramVersions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=50)),
                ('field2', models.IntegerField()),
                ('field3', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Program')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
