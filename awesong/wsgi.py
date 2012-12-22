import os, sys, django.core.handlers.wsgi
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'awesong.settings'
application = django.core.handlers.wsgi.WSGIHandler()