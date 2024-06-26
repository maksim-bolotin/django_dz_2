# Generated by Django 5.0.4 on 2024-06-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=200, verbose_name='URL')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Изображение')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата записи')),
                ('publication_sign', models.BooleanField(default=True, verbose_name='Публикация')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
        ),
    ]
