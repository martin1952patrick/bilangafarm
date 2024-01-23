# Generated by Django 3.2.9 on 2021-12-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
