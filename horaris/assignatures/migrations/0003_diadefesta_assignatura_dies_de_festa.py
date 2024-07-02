# Generated by Django 4.2 on 2024-07-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignatures', '0002_assignatura_data_inici'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaDeFesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('data', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='assignatura',
            name='dies_de_festa',
            field=models.ManyToManyField(blank=True, to='assignatures.diadefesta'),
        ),
    ]
