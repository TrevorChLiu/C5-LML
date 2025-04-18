# Generated by Django 5.1.7 on 2025-04-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_art', models.ImageField(blank=True, null=True, upload_to='forum_images/')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('popularity', models.BigIntegerField(default=0)),
                ('description', models.TextField()),
            ],
        ),
    ]
