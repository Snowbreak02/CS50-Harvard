from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.CharField(choices=[('BOOK', 'Book'), ('CODE', 'Code'), ('CRS', 'Course'), ('DOC', 'Document'), ('QUIZ', 'Quiz'), ('VID', 'Video')], max_length=4),
        ),
    ]
