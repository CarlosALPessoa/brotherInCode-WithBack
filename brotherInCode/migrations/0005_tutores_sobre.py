# Generated by Django 4.2.1 on 2023-05-31 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brotherInCode', '0004_alter_alunos_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutores',
            name='sobre',
            field=models.TextField(blank=True, null=True),
        ),
    ]