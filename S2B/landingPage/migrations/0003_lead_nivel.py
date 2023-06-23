# Generated by Django 3.2.19 on 2023-06-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0002_lead_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='nivel',
            field=models.CharField(choices=[('1', 'Básico'), ('2', 'Intermediário'), ('3', 'Avançado')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
