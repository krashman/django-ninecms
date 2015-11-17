""" Node system utility functions """
__author__ = 'George Karakostas'
__copyright__ = 'Copyright 2015, George Karakostas'
__licence__ = 'BSD-3'
__email__ = 'gkarak@9-dev.com'

from django.conf import settings


def get_full_path(path, language, bookmark=''):
    """ Utility function to build a valid path based on an initial
    :param path: the initial path
    :param language: language component
    :param bookmark: bookmark, if any
    :return: a valid path string
    """
    if not path.startswith('/'):
        path = '/' + path
    if not path.endswith('/'):
        path += '/'
    path += bookmark
    if language and settings.I18N_URLS:  # pragma: nocover
        path = '/' + language + path
    return path
