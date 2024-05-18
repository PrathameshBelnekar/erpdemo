# Generated by Django 4.2.5 on 2024-04-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(choices=[('Percentage', 'Percentage'), ('Fixed Amount', 'Fixed Amount')], max_length=50)),
                ('discount_value', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]