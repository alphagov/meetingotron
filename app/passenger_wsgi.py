import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, root)

activate_this = os.path.join(root, '../../../shared/virtualenv/bin/activate_this.py') 
execfile(activate_this, dict(__file__=activate_this))

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
