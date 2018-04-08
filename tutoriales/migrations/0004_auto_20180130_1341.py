# Generated by Django 2.0.1 on 2018-01-30 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriales', '0003_leccion_length'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serietutoriales',
            old_name='experianciaEstudiante',
            new_name='experiancia_estudiante',
        ),
        migrations.AlterField(
            model_name='leccion',
            name='serie_tutoriales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutoriales', to='tutoriales.SerieTutoriales'),
        ),
    ]