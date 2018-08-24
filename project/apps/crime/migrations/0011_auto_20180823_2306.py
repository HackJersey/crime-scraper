# Generated by Django 2.0.7 on 2018-08-23 23:06

from django.db import migrations, models
import django.db.models.deletion
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0010_crimereport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scraped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_hash', models.TextField(blank=True, null=True)),
                ('s3_url', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True, unique=True, verbose_name='ScrapeURL')),
                ('scraped_date', models.DateTimeField(auto_now_add=True)),
                ('status_code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapeSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', url_or_relative_url_field.fields.URLOrRelativeURLField(blank=True, null=True, unique=True, verbose_name='ScrapeURL')),
                ('name', models.CharField(max_length=200)),
                ('selector', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='scraped',
            name='source_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crime.ScrapeSite'),
        ),
    ]
