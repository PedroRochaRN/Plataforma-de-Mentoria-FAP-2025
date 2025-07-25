# Generated by Django 5.2 on 2025-07-04 00:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorados', '0006_tarefa_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaIA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duvida', models.TextField()),
                ('resposta', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mentorado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorados.mentorados')),
            ],
            options={
                'verbose_name': 'Consulta IA',
                'verbose_name_plural': 'Consultas IA',
                'ordering': ['-created_at'],
            },
        ),
    ]
