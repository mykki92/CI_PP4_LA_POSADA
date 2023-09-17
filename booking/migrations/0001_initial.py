# Generated by Django 3.2.21 on 2023-09-17 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('booking_date', models.DateField()),
                ('booking_time', models.CharField(choices=[('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00')], max_length=25)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default='', max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Rejected', 'Rejected'), ('Expired', 'Expired')], default='pending', max_length=25)),
                ('party_of', models.IntegerField(choices=[(1, '1 Guest'), (2, '2 Guests'), (3, '3 Guests'), (4, '4 Guests'), (5, '5 Guests'), (6, '6 Guests'), (7, '7 Guests'), (8, '8 Guests')], default=2)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-booking_time'],
                'unique_together': {('booking_date', 'booking_time')},
            },
        ),
    ]
