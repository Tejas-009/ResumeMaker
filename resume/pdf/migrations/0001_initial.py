# Generated by Django 4.1 on 2022-09-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('phone', models.CharField(default='', max_length=10)),
                ('add', models.CharField(default='', max_length=50)),
                ('dob', models.CharField(default='', max_length=10)),
                ('gen', models.CharField(default='', max_length=50)),
                ('lang', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('university', models.CharField(default='', max_length=20)),
                ('course', models.CharField(default='', max_length=20)),
                ('year', models.CharField(default='', max_length=20)),
                ('perc', models.CharField(default='', max_length=20)),
                ('college', models.CharField(default='', max_length=20)),
                ('course1', models.CharField(default='', max_length=20)),
                ('year1', models.CharField(default='', max_length=20)),
                ('perc1', models.CharField(default='', max_length=20)),
                ('skills', models.TextField(default='', max_length=20)),
                ('img', models.ImageField(default='', upload_to='pdf/media')),
                ('career', models.TextField(default='', max_length=400)),
                ('strength', models.TextField(default='', max_length=200)),
                ('area', models.CharField(default='', max_length=200)),
            ],
        ),
    ]