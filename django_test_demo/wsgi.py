import os
from django.core.wsgi import get_wsgi_application

environment = os.environ.get('ENVIRONMENT')
if environment == 'production':
    config = 'django_test_demo.settings.prod'
elif environment == 'development':
    config = 'django_test_demo.settings.dev'
elif environment == 'staging':
    config = 'django_test_demo.settings.stg'
else:
    config = 'django_test_demo.settings.common'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config)

application = get_wsgi_application()