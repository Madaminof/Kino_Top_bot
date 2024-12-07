import os
from django.core.wsgi import get_wsgi_application

# Django konfiguratsiyasini yuklash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kinobot.settings')

# Django ilovasini ishga tushurish
application = get_wsgi_application()

# Botni ishga tushurish (agar kerak bo'lsa)
import Kinobot.bot_app.bot
