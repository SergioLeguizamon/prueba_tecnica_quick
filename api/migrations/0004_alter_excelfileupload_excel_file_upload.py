# Generated by Django 3.2.7 on 2021-12-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_excelfileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfileupload',
            name='excel_file_upload',
            field=models.FileField(upload_to='static/excel'),
        ),
    ]
