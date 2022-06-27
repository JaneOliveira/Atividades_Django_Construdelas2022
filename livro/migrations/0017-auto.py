import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0016_emprestimos_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 28, 16, 31, 54, 316129)),
        ),
    ]