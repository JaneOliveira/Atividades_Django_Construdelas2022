from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_auto_20210805_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now=True),
        ),
    ]