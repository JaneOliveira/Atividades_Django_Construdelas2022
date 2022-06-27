from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_ativo'),
        ('livro', '0006_auto_20210819_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]