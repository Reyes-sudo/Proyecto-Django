import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SQLITE={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

