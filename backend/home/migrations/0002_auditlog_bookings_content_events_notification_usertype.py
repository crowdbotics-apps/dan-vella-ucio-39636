# Generated by Django 2.2.28 on 2023-04-11 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateTimeField()),
                ('state', models.IntegerField()),
                ('address', models.TextField()),
                ('tickets_sold', models.BooleanField()),
                ('ticketID', models.IntegerField()),
                ('event_typeID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField()),
                ('mobile', models.IntegerField()),
                ('roleID', models.IntegerField()),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usertype_userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeID', models.IntegerField()),
                ('title', models.TextField()),
                ('bodytext', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('duedate', models.DateField()),
                ('datecreated', models.DateTimeField()),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_eventID', to='home.Events')),
            ],
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.BigIntegerField()),
                ('objectID', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('recordID', models.IntegerField()),
                ('action', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditlog_userID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
