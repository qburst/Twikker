# Generated by Django 4.1.2 on 2022-11-06 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_alter_like_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweek',
            name='retweek',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='retweeks', to='feed.tweek'),
        ),
    ]
