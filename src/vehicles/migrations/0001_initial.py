# Generated by Django 4.2.1 on 2023-05-05 19:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Марка транспортного средства',
                'verbose_name_plural': 'Марки Транспортных средств',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Цвет Автотранспорта',
                'verbose_name_plural': 'Цвета Автотранспорта',
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер распределения')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата распределения')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Распределение',
                'verbose_name_plural': 'Распределения',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер Двигателя')),
                ('model', models.CharField(blank=True, max_length=15, null=True, verbose_name='Модель двигателя т/c')),
                ('power', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Мощность двигателя т/c')),
                ('capacity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Объем двигателя т/с')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Двигатель Т/C',
                'verbose_name_plural': 'Двигатели Т/C',
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Марка Бензина',
                'verbose_name_plural': 'Марки бензина',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Служба эксплуатации автомобиля',
                'verbose_name_plural': 'Службы эксплутации автомобиля',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Завод Изготовитель',
                'verbose_name_plural': 'Заводы Изготовителя',
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер тех. паспорта')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи тех. паспорта')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тех. паспорт',
                'verbose_name_plural': 'Тех. паспорта',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Организ., выдавшая наряд',
                'verbose_name_plural': 'Организ., выдавшая наряд',
            },
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(blank=True, max_length=35, null=True, verbose_name='Название Подразделения')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Телефон')),
                ('chief', models.CharField(blank=True, max_length=35, null=True, verbose_name='Начальник Подразделения')),
                ('percent_city', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Процент города')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.subdivision')),
            ],
            options={
                'verbose_name': 'Подразделение-владелец транспорта',
                'verbose_name_plural': 'Подразделения-владельцы транспорта',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('avatar', models.ImageField(blank=True, default='images/default.png', upload_to='images/vehicles/')),
                ('inventory_number', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Инвентарный номер')),
                ('chass_number', models.CharField(blank=True, max_length=8, null=True, verbose_name='Номер Шасси')),
                ('body_number', models.CharField(blank=True, max_length=8, null=True, verbose_name='Номер Кузова')),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Год выпуска')),
                ('gov_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер государственной регистрации')),
                ('register_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Реестровый номер')),
                ('sign_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи номерного знака')),
                ('exploitation_date', models.DateField(blank=True, null=True, verbose_name='Дата ввода в эксплутацию')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Балансовая стоимость')),
                ('source_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер Фондового извещения')),
                ('source_date', models.DateField(blank=True, null=True, verbose_name='Дата документа')),
                ('transfer_date', models.DateField(blank=True, null=True, verbose_name='Дата передачи в подразделение')),
                ('del_date', models.DateField(blank=True, null=True, verbose_name='Дата списания')),
                ('mileage_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Месячная норма пробега')),
                ('fuel_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Норма расхода топлива на 100 км')),
                ('id_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Идентификационный номер')),
                ('climate_control', models.BooleanField(blank=True, null=True, verbose_name='Наличие системы Климат контроль')),
                ('base_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Базовая норма расхода топлива')),
                ('identifier_fuel_rate', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Инд. процент баз. нормы расхода топлива')),
                ('category', models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1, null=True, verbose_name='Категория автомобиля')),
                ('trust_date', models.DateField(blank=True, null=True, verbose_name='Дата действия страхавого полиса')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='Дата действия технического осмотра')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тип транспортного средства',
                'verbose_name_plural': 'Типы Транспортных средств',
            },
        ),
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('image', models.ImageField(upload_to='images/vehicles/')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ManyToManyField(blank=True, related_name='images', to='vehicles.vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Штатная группа',
                'verbose_name_plural': 'Штатные группы',
            },
        ),
        migrations.CreateModel(
            name='VehicleFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('file', models.FileField(upload_to='files/vehicles/')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ManyToManyField(blank=True, related_name='files', to='vehicles.vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Класс Автотранспорта',
                'verbose_name_plural': 'Классы Автотранспорта',
            },
        ),
        migrations.CreateModel(
            name='VehicleBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(blank=True, max_length=2, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тип Кузова',
                'verbose_name_plural': 'Тип Кузовов',
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehiclebody', verbose_name='Тип Кузова'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.brand', verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.color', verbose_name='Цвет автомобиля'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='distribution',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.distribution', verbose_name='Распределение'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.engine', verbose_name='Двигатель Т/С'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.fueltype', verbose_name='Марка бензина'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehiclegroup', verbose_name='Штатная группа'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.manufacturer', verbose_name='Завод-Изготовитель'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='passport',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.passport', verbose_name='Тех. паспорт'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.maintenanceservice', verbose_name='Служба эксплутации'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.source', verbose_name='Источник получения'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='subdivision',
            field=models.ForeignKey(blank=True, db_column='owner', null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.subdivision', verbose_name='Подразделение-владелец транспорта'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicletype', verbose_name='Тип транспорта'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_class',
            field=models.ForeignKey(blank=True, db_column='class', null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicleclass', verbose_name='Класс автомобиля'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.warehouse', verbose_name='Склад'),
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата удаления')),
                ('date', models.DateTimeField()),
                ('value', models.IntegerField(verbose_name='Показания счетчика')),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counters', to='vehicles.vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]