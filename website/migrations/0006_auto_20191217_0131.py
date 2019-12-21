# Generated by Django 2.2.4 on 2019-12-17 01:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20191217_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedormodel',
            name='cep',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='cadastrosite',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 1, 31, 38, 198659, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cadastrosite',
            name='dataNasc',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 1, 31, 38, 198620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cidademodel',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 1, 31, 38, 152891, tzinfo=utc)),
        ),
    ]