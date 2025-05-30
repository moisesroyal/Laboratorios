# Generated by Django 5.2.1 on 2025-05-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secante_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secanteresultado',
            old_name='iteraciones_usadas',
            new_name='max_iter',
        ),
        migrations.RenameField(
            model_name='secanteresultado',
            old_name='tolerancia',
            new_name='tol',
        ),
        migrations.RemoveField(
            model_name='secanteresultado',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='secanteresultado',
            name='max_iteraciones',
        ),
        migrations.AddField(
            model_name='secanteresultado',
            name='iteraciones',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='secanteresultado',
            name='resultado_grafico',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='secanteresultado',
            name='raiz',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
