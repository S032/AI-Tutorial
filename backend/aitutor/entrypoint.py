#!/usr/bin/env python
import os
import sys
import django
from django.core.management import call_command
from django.contrib.auth import get_user_model

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aitutor.settings')
django.setup()

User = get_user_model()


def create_superuser_():
    # Значения по умолчанию с информативными сообщениями
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')

    # Информативные сообщения о значениях по умолчанию
    if username == 'admin':
        print(
            "⚠️ Using default username 'admin'. Consider setting DJANGO_SUPERUSER_USERNAME")
    if email == 'admin@example.com':
        print("⚠️ Using default email 'admin@example.com'. Consider setting DJANGO_SUPERUSER_EMAIL")
    if password == 'adminpassword':
        print(
            "⚠️ Using default password. This is NOT SECURE! Set DJANGO_SUPERUSER_PASSWORD")

    try:
        # Попытка создать суперпользователя
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superuser {username} created successfully")
    except django.db.utils.IntegrityError:
        # Если пользователь уже существует
        print(f"ℹ️ Superuser {username} already exists")


def main():
    print("🔄 Applying database migrations...")
    call_command('migrate')

    # Попытка создания суперпользователя
    create_superuser_()

    # Запуск сервера
    print("🚀 Starting Django development server...")
    from django.core.management.commands.runserver import Command as RunserverCommand
    RunserverCommand().run_from_argv(
        ['manage.py', 'runserver', '0.0.0.0:8000'])


if __name__ == '__main__':
    main()
