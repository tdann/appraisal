# Generated by Django 3.2.5 on 2021-08-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffappraisal', '0004_auto_20210730_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appraiseecomment',
            name='competence',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staffappraisal.competence'),
        ),
    ]
