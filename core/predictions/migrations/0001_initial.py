# Generated by Django 4.1.7 on 2023-10-20 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PresupuestoServicios',
            fields=[
                ('id_presupuesto_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_servicio', models.CharField(max_length=20)),
                ('fecha_servicio', models.DateField()),
                ('fecha_caducidad_servicio', models.DateField()),
                ('tipo_descuento_servicio', models.CharField(max_length=22)),
                ('monto_descuento_servicio', models.DecimalField(decimal_places=2, max_digits=18)),
                ('con_sin_igv_servicio', models.CharField(max_length=15)),
                ('sub_total_servicio', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_impuesto_servicio', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('total_servicio', models.DecimalField(decimal_places=2, max_digits=18)),
                ('estado_servicio', models.CharField(max_length=22)),
                ('referencia_servicio', models.CharField(max_length=100, null=True)),
                ('nota_admin_servicio', models.CharField(max_length=6000, null=True)),
                ('nota_cliente_servicio', models.CharField(max_length=6000, null=True)),
                ('terminos_condiciones_servicio', models.CharField(max_length=2000, null=True)),
                ('tipo_monto_descuento', models.CharField(max_length=100, null=True)),
                ('monto_descuento_oficial', models.DecimalField(decimal_places=0, max_digits=20, null=True)),
                ('empleado_id', models.IntegerField()),
                ('perfil_cliente_id', models.IntegerField()),
                ('impuesto_id', models.IntegerField()),
                ('moneda_id', models.IntegerField()),
                ('sede_id', models.IntegerField(null=True)),
                ('empresa_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicacionesFacebook',
            fields=[
                ('id_publicacion', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo_publicacion', models.TextField()),
                ('Descripcion_publicacion', models.TextField(null=True)),
                ('imagen_publicacion', models.TextField(null=True)),
                ('servicio_referencia', models.TextField(null=True)),
                ('comentarios', models.IntegerField(default=0)),
                ('fecha_publicacion', models.DateField(null=True)),
                ('hora_publicacion', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=250)),
                ('descripcion_servicio', models.TextField(null=True)),
                ('precio_servicio', models.DecimalField(decimal_places=2, max_digits=18)),
                ('categoria_id', models.IntegerField()),
                ('unidad_medida_id', models.IntegerField()),
                ('activo_servicio', models.IntegerField()),
                ('empresa_id', models.IntegerField()),
                ('sede_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PresupuestoDetallesServicios',
            fields=[
                ('id_presupuesto_detalle_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_presup_det_ser', models.CharField(max_length=100)),
                ('cantidad_presup_det_ser', models.IntegerField()),
                ('precio_venta_presup_det_ser', models.DecimalField(decimal_places=2, max_digits=18)),
                ('importe_venta_presup_det_ser', models.DecimalField(decimal_places=2, max_digits=18)),
                ('presupuesto_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predictions.presupuestoservicios')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predictions.servicios')),
            ],
        ),
    ]