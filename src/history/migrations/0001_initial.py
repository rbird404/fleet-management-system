# Generated by Django 4.2 on 2023-05-02 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('field', models.CharField(max_length=32)),
                ('value', models.TextField(blank=True, null=True)),
                ('value_type', models.CharField(choices=[('int', 'int'), ('date', 'date'), ('bool', 'bool'), ('decimal', 'decimal'), ('str', 'str'), ('none', 'none')], max_length=8)),
                ('created_at', models.DateField(null=True, verbose_name='Дата ввода')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'История изменений',
                'verbose_name_plural': 'История изменений',
            },
        ),
    ]
