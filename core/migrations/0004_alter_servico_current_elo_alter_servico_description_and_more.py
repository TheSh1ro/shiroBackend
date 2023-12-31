# Generated by Django 4.2.7 on 2023-12-08 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_servico_payment_method_alter_servico_queue_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servico",
            name="current_elo",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="servico",
            name="description",
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="servico",
            name="queue",
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to="core.fila"),
        ),
        migrations.AlterField(
            model_name="servico",
            name="riot_tag",
            field=models.CharField(default="#BR1", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="servico",
            name="status",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="servicos_status",
                to="core.status",
            ),
        ),
        migrations.AlterField(
            model_name="servico",
            name="target_elo",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="servico",
            name="time",
            field=models.IntegerField(max_length=2, null=True),
        ),
    ]
