# Generated by Django 4.2.1 on 2023-05-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('judul', models.CharField(blank=True, max_length=200, primary_key=True, serialize=False)),
                ('pengarang', models.CharField(blank=True, max_length=200, null=True)),
                ('isbn', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
