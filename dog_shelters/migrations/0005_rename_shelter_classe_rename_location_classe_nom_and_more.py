# Generated by Django 4.1.5 on 2024-03-20 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0004_delete_bibliotheque_delete_document_delete_membre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shelter',
            new_name='Classe',
        ),
        migrations.RenameField(
            model_name='classe',
            old_name='location',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='classe',
            old_name='name',
            new_name='specialite',
        ),
    ]
