# -*- coding: utf-8 -*-
import os, sys
<<<<<<< HEAD
sys.path.insert(0, '/home/d/drimspb/drugoekino.top/public_html')
=======
sys.path.insert(0, '/home/d/drimspb/drugoekino.top')
>>>>>>> d8a94bd48dad1951c6f1afbce07b17864954c3d5
sys.path.insert(1, '/home/d/drimspb/.local/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()