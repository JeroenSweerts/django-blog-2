# Generated by Django 2.1.1 on 2019-10-31 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAdmin2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='modeladmin2',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.Category'),
        ),
        migrations.AddField(
            model_name='modeladmin2',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.Post'),
        ),
    ]