from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0003_comment_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='embeddable',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
