# Generated by Django 4.1.4 on 2022-12-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excel_doc_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_one', models.FileField(upload_to='saved/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Excel_doc_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_two', models.FileField(upload_to='saved/%Y/%m/%d/')),
            ],
        ),
    ]
