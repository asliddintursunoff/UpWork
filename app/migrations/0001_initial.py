# Generated by Django 3.2.16 on 2023-01-27 17:20

import app.manager
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('about', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': "Bo'lim ",
                'verbose_name_plural': "Bo'limlar ",
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=200)),
                ('specialty', models.CharField(max_length=1000)),
                ('staffka', models.IntegerField()),
                ('phone', models.CharField(help_text=' +998 bilan kiriting', max_length=13)),
                ('bulim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization')),
            ],
            options={
                'verbose_name': 'Ishchi ',
                'verbose_name_plural': 'Ishchilar  ',
            },
        ),
        migrations.CreateModel(
            name='Worker_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('information', models.CharField(max_length=200)),
                ('graduated_university', models.CharField(blank=True, help_text='if worker studied university , you can fill out this space,else not', max_length=1000, null=True)),
                ('magistratura', models.CharField(blank=True, help_text='if worker studied magistratura , you can fill out this space,else not', max_length=1000, null=True)),
                ('know_languages', models.CharField(max_length=200)),
                ('describtion', models.TextField(help_text='about worker')),
                ('FIO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.worker')),
            ],
            options={
                'verbose_name': 'Ishchi malumoti ',
                'verbose_name_plural': 'Ishchilar malumoti ',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qarindoshligi', models.CharField(help_text='Kim ekanini kiriting.....', max_length=500)),
                ('qarindosh_ismi', models.CharField(help_text='Qarindoshni kiriting.....', max_length=500)),
                ('qarindosh_tug_yil', models.DateField()),
                ('yashash_joyi', models.CharField(help_text='Yashash manzil...', max_length=500)),
                ('ish_joyi', models.CharField(help_text='Ish manzil...', max_length=500)),
                ('hodim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.worker_about')),
            ],
            options={
                'verbose_name': 'Qarindoshi',
                'verbose_name_plural': 'Qarindoshlari',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=6)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('object', app.manager.UserManager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
