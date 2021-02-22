# Generated by Django 3.1.6 on 2021-02-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '커뮤니티 사용자', 'verbose_name_plural': '커뮤니티 사용자'},
        ),
        migrations.AddField(
            model_name='user',
            name='useremail',
            field=models.EmailField(default=1, max_length=100, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
