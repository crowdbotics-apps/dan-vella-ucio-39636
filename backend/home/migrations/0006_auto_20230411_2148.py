# Generated by Django 2.2.28 on 2023-04-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20230411_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditlog',
            name='objectID',
        ),
        migrations.RemoveField(
            model_name='content',
            name='body',
        ),
        migrations.AddField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='content',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.TextField(blank=True),
        ),
    ]