# Generated by Django 4.2.1 on 2023-09-29 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('english', models.PositiveIntegerField(choices=[(1, 'One Field'), (2, 'Two Fields')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Anglai',
            fields=[
                ('grade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='a3ded.grade')),
                ('oral', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
            bases=('a3ded.grade',),
        ),
        migrations.CreateModel(
            name='Arbi',
            fields=[
                ('grade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='a3ded.grade')),
                ('chifehi', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('kira2a', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('intej', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
            bases=('a3ded.grade',),
        ),
        migrations.CreateModel(
            name='Francai',
            fields=[
                ('grade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='a3ded.grade')),
                ('exp', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('lecture', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('production', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
            bases=('a3ded.grade',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a3ded.schoolclass')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a3ded.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a3ded.schoolclass')),
            ],
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='teachers',
            field=models.ManyToManyField(to='a3ded.teacher'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a3ded.student'),
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a3ded.subject'),
        ),
        migrations.AddField(
            model_name='grade',
            name='trimestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a3ded.trimestre'),
        ),
    ]
