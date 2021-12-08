# Generated by Django 3.2.9 on 2021-12-08 15:47

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, unique, max-255', max_length=255, unique=True, verbose_name='brand name')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max-100', max_length=110, verbose_name='category_name')),
                ('slug', models.SlugField(help_text='format: required, letters, numbers, underscore,hyphen', max_length=150, verbose_name='category_safe_URL')),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='format: not required', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='inventory.category', verbose_name='parent of category')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_id', models.CharField(help_text='format: required, unique', max_length=50, unique=True, verbose_name='product website ID')),
                ('slug', models.SlugField(help_text='format: required, letters, numbers, underscores or hyphens', max_length=255, verbose_name='product safe URL')),
                ('name', models.CharField(help_text='format: required, max-255', max_length=255, verbose_name='product name')),
                ('description', models.TextField(help_text='format: required', verbose_name='product description')),
                ('is_active', models.BooleanField(default=True, help_text='format: true=product visible', verbose_name='product visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='date product created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='date product last updated')),
                ('category', mptt.fields.TreeManyToManyField(to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, unique, max-255', max_length=255, unique=True, verbose_name='type of product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(help_text='format: required, unique, max-20', max_length=20, unique=True, verbose_name='stock keeping unit')),
                ('upc', models.CharField(help_text='format: required, unique, max-12', max_length=12, unique=True, verbose_name='universal product code')),
                ('is_active', models.BooleanField(default=True, help_text='format: true=product visible', verbose_name='product visibility')),
                ('retail_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'the price must be between 0 and 999.99.'}}, help_text='format: maximum price 999.99', max_digits=5, verbose_name='recommended retail price')),
                ('store_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'the price must be between 0 and 999.99.'}}, help_text='format: maximum price 999.99', max_digits=5, verbose_name='regular store price')),
                ('sale_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'the price must be between 0 and 9999999.99.'}}, help_text='format: maximum price 9999999.99', max_digits=9, verbose_name='sale price')),
                ('weight', models.FloatField(verbose_name='product weight')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='date sub-product created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='date sub-product updated')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand', to='inventory.brand')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='inventory.product')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_type', to='inventory.producttype')),
            ],
        ),
    ]