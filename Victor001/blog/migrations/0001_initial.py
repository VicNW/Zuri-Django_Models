# Generated by Django 4.0.5 on 2022-06-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Text', models.TextField()),
                ('Created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]