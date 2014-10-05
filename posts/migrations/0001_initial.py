# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField(max_length=200)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField(null=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('date_modif', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_auth', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('phone', models.CharField(null=True, default=None, max_length=20, verbose_name='Phone number', blank=True)),
                ('date_born', models.DateField(null=True, default=None, verbose_name='Born Date', blank=True)),
                ('last_connexion', models.DateTimeField(null=True, default=None, verbose_name='Date of last connexion', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('userprofile_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='posts.UserProfile', serialize=False, auto_created=True)),
                ('specialisation', models.CharField(verbose_name='Specialisation', max_length=50)),
            ],
            options={
            },
            bases=('posts.userprofile',),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(to='posts.Publisher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='posts.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='posts.Publisher'),
            preserve_default=True,
        ),
    ]
