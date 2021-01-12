version_info = (0, 8, 11, 6)

__version__ = version = '.'.join(map(str, version_info))
__project__ = PROJECT = 'django-summernote'
__author__ = AUTHOR = "django-summernote contributors"

from django import VERSION as django_version
if django_version < (3, 2):
    default_app_config = 'django_summernote.apps.DjangoSummernoteConfig'
