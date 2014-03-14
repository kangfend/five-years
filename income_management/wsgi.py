import os, socket, sys

HOSTNAME = socket.gethostname()
PRODUCTION_SERVERS = ['code-latte.com','playwithapro.com','li651-164']


if HOSTNAME in PRODUCTION_SERVERS:
    LIVEHOST = True
else:
    LIVEHOST = False

if LIVEHOST:
  if HOSTNAME == 'code-latte.com':
    sys.path.append('/usr/local/lib/python2.7/site-packages')
    sys.path.append('/home/benny/Envs/django_env/lib/python2.7/site-packages')
    sys.path.append('/home/benny/Envs/django_env/src')
    sys.path.append('/home/benny/public_html/five')
  else:
    sys.path.append('/home/pwap/python_envs/django/lib/python2.7/site-packages')
    sys.path.append('/home/pwap/python_envs/django/src')
    sys.path.append('/home/pwap/public_html/five')
else:
    sys.path.append('/Users/bennychristanto/Development/Django_Envs/env_django151/lib/python2.7/site-packages')
    sys.path.append('/Users/bennychristanto/Sites/income_management/income_management')

os.environ["DJANGO_SETTINGS_MODULE"] = "income_management.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
