# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-26 08:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdbmeta', '0012_auto_20180329_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdbrecord',
            name='atomic_number',
            field=models.PositiveSmallIntegerField(help_text='Example: 74 [for a tungsten PKA]', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(118)], verbose_name='Projectile / PKA atomic number'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='attribution',
            field=models.ForeignKey(help_text='Person, publication DOI, comments and acknowledgements', on_delete=django.db.models.deletion.CASCADE, to='cdbmeta.Attribution'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='box_X',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Box X-length /Å'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='box_X_orientation',
            field=models.CharField(blank=True, help_text='As Miller indices, e.g. (100)', max_length=15, verbose_name='Box X-orientation'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='box_Y',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Box Y-length /Å'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='box_Y_orientation',
            field=models.CharField(blank=True, help_text='As Miller indices, e.g. (010)', max_length=15, verbose_name='Box Y-orientation'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='box_Z',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Box Z-length /Å'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='box_Z_orientation',
            field=models.CharField(blank=True, help_text='As Miller indices, e.g. (001)', max_length=15, verbose_name='Box Z-orientation'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='code_name',
            field=models.CharField(help_text='e.g. "LAMMPS"', max_length=100),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='code_version',
            field=models.CharField(help_text='e.g. "22 Aug 2018"', max_length=20),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='electronic_stopping',
            field=models.BooleanField(default=False, verbose_name='Is electronic stopping included?'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='energy',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Projectile / PKA energy /keV'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='has_surface',
            field=models.BooleanField(default=False, verbose_name='Does the simulation include a surface?'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='initially_perfect',
            field=models.BooleanField(default=True, verbose_name='Is the crystal initially perfect?'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='input_filename',
            field=models.CharField(blank=True, help_text='If provided, the filename of the .xyz file giving the initial state of the material in the simulation', max_length=100),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='interatomic_potential_filename',
            field=models.CharField(blank=True, help_text='If provided, the filename or URL to a resource providing the interatomic potential(s) used in the simulation', max_length=100),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='material',
            field=models.ForeignKey(help_text='Chemical formula, structure and lattice parameters', on_delete=django.db.models.deletion.CASCADE, to='cdbmeta.Material'),
        ),
        migrations.AlterField(
            model_name='cdbrecord',
            name='thermostat',
            field=models.BooleanField(default=False, verbose_name='Is a thermostat included?'),
        ),
    ]