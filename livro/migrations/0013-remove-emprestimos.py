from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_alter_emprestimos_tempo_duracao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='tempo_duracao',
        ),
    ]