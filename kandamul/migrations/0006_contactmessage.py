# Generated by Django 5.1.7 on 2025-03-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kandamul', '0005_remove_testimonial_name_testimonial_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
