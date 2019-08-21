# pylint: disable=W0614,W0401
"""Setup database for tests"""


from config.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'summer_pr_db_test',

    }
}
