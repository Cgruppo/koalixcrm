# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-16 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20180116_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('salesdocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.SalesDocument')),
                ('status', models.CharField(choices=[('O', 'Ordered'), ('D', 'Delayed'), ('Y', 'Delivered'), ('I', 'Invoice registered'), ('P', 'Invoice payed')], max_length=1)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Payment Reminder',
                'verbose_name_plural': 'Payment Reminders',
            },
            bases=('crm.salesdocument',),
        ),
    ]
