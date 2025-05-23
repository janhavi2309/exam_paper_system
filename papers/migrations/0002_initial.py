# Generated by Django 5.1.6 on 2025-04-28 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('papers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='decryptionrequest',
            name='moderator',
            field=models.ForeignKey(limit_choices_to={'role': 'Moderator'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moderationreview',
            name='moderator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paper',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'role': 'Teacher'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moderationreview',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.paper'),
        ),
        migrations.AddField(
            model_name='finalselection',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.paper'),
        ),
        migrations.AddField(
            model_name='decryptionrequest',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.paper'),
        ),
    ]
