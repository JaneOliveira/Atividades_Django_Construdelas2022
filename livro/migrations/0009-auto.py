from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_ativo'),
        ('livro', '0008_auto_20210826_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='nome_emprestado_anonimo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='nome_emprestado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]