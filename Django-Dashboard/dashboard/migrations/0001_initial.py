from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
                ('target', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]
