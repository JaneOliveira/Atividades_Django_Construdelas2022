from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_auto_20210826_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='tempo_duracao',
            field=models.TimeField(blank=True, null=True),
        ),
    ]