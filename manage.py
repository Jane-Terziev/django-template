#!/usr/bin/env python
import os
import sys

environment = os.environ.get('ENVIRONMENT')
if environment == 'production':
    config = 'django_test_demo.settings.prod'
elif environment == 'development':
    config = 'django_test_demo.settings.dev'
elif environment == 'staging':
    config = 'django_test_demo.settings.staging'
else:
    config = 'django_test_demo.settings.common'


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', config)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
