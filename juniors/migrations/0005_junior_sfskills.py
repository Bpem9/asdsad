# Generated by Django 3.2.15 on 2022-10-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juniors', '0004_alter_junior_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='junior',
            name='sfskills',
            field=models.ManyToManyField(null=True, to='juniors.SoftSkills', verbose_name='Софт-скиллы'),
        ),
    ]