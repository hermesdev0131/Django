version_info = (0, 8, 20, 0)

__version__ = version = '.'.join(map(str, version_info))
__project__ = PROJECT = 'django-summernote'
__author__ = AUTHOR = "django-summernote contributors"

try:
    from django import VERSION as django_version
    if django_version < (3, 2):
        default_app_config = 'django_summernote.apps.DjangoSummernoteConfig'
except ModuleNotFoundError:
    # This part is needed for setup.py
    pass
