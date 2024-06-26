# Generated by Django 4.1.5 on 2023-01-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliotheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.TextField(unique=True)),
                ('nom', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.TextField()),
                ('auteur', models.TextField()),
                ('isbn', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.TextField(unique=True)),
                ('nom', models.TextField()),
                ('numero', models.IntegerField()),
                ('NombreLivreEmprunte', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='dog',
            name='adoption_date',
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(),
        ),
    ]
