from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0013_remove_emprestimos_tempo_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.livros'),
        ),
    ]