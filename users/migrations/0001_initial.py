# Generated by Django 3.2 on 2021-04-18 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=16)),
                ('phone_number', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=15)),
                ('previous_payment', models.DecimalField(decimal_places=2, max_digits=14)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'user_ranks',
            },
        ),
        migrations.CreateModel(
            name='VoucherType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'voucher_types',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=30)),
                ('expiration_date', models.DateTimeField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('voucher_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.vouchertype')),
            ],
            options={
                'db_table': 'vouchers',
            },
        ),
        migrations.CreateModel(
            name='UserVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_used', models.SmallIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('voucher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.voucher')),
            ],
            options={
                'db_table': 'user_vouchers',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='user_rank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.userrank'),
        ),
        migrations.AddField(
            model_name='user',
            name='voucher',
            field=models.ManyToManyField(through='users.UserVoucher', to='users.Voucher'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
    ]
