# Generated by Django 2.2 on 2020-12-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(help_text='用户名由英文字母、下划线数字组成', max_length=10, verbose_name='用户名')),
                ('password', models.CharField(help_text='登录密码由6-8位字符组成', max_length=6, verbose_name='密码')),
                ('email', models.CharField(help_text='有效电子邮箱地址', max_length=30, verbose_name='Email')),
            ],
        ),
    ]
