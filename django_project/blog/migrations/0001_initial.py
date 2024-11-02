from django.conf import settings
from django.db import migrations, models
from django.db.models.deletion
from django.utils.timezone

class Migration(migrations.Migration):
    initial - True

    dependencies =[
        migrations.swappable_dependency(settings.AUTH_USER_MODEL)
    ]

operations = [
    migrations.CreateModel(
        name='post',
        fields=[
('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
('title', models.CharField(max_length=100)),
('content', models.TextField()),
('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
 ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTTH_USER_MODEL)),
        ],
    ),
]
class Product(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
