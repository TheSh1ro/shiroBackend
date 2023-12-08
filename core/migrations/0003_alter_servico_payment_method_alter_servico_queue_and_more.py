# Generated by Django 4.2.7 on 2023-12-08 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_status_remove_servico_completed_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servico",
            name="payment_method",
            field=models.CharField(default="Pix", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="servico",
            name="queue",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="core.fila"),
        ),
        migrations.AlterField(
            model_name="servico",
            name="service",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="servicos_type",
                to="core.modalidade",
            ),
        ),
    ]
