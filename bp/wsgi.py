import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/u0000006/data/www/faq-reg.ru/project_name')
sys.path.insert(1, '/var/www/u0000006/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bp.settings'

application = get_wsgi_application()
