# Generated by Django 5.1 on 2024-08-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_opcao_1_escolher_opcoes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escolher',
            old_name='opcoes',
            new_name='opcao_1',
        ),
        migrations.AddField(
            model_name='escolher',
            name='opcao_2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escolher',
            name='opcao_3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escolher',
            name='opcao_4',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
