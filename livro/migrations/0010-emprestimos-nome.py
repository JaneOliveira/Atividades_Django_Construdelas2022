from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_ativo'),
        ('livro', '0009_auto_20210826_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='nome_emprestado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
       