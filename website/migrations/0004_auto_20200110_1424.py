# Generated by Django 2.2.4 on 2020-01-10 14:24

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200110_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='contaPagarModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.CharField(blank=True, max_length=300, null=True)),
                ('dataVencimento', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('1', 'Em aberto'), ('2', 'Paga'), ('3', 'Atrasada'), ('4', 'Cancelada')], default=1, max_length=1)),
                ('fixa', models.CharField(choices=[('1', 'Sim'), ('2', 'Nao')], default=1, max_length=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='contaReceberModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.CharField(blank=True, max_length=300, null=True)),
                ('dataVencimento', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('1', 'Em aberto'), ('2', 'Paga'), ('3', 'Atrasada'), ('4', 'Cancelada')], default=1, max_length=1)),
                ('fixa', models.CharField(choices=[('1', 'Sim'), ('2', 'Nao')], default=1, max_length=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='cadastrosite',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 14, 24, 34, 60521, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cadastrosite',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 14, 24, 34, 60504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 10, 14, 24, 34, 40369, tzinfo=utc)),
        ),
    ]