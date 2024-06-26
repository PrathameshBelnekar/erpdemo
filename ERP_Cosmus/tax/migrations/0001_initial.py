# Generated by Django 4.2.5 on 2024-04-25 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('GST', 'GST'), ('VAT', 'VAT'), ('Sales Tax', 'Sales Tax')], max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaxRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField()),
                ('description', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventorylocation')),
                ('tax_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tax.taxcategory')),
            ],
        ),
        migrations.CreateModel(
            name='TaxExemption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_type', models.CharField(max_length=255)),
                ('entity_id', models.IntegerField()),
                ('reason', models.TextField()),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField()),
                ('tax_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tax.taxrate')),
            ],
        ),
        migrations.CreateModel(
            name='TaxCalculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tax_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tax.taxrate')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tax_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tax.taxrate')),
            ],
        ),
    ]
