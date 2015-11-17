import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ninecms',
    version='0.5.0',
    packages=['ninecms'],
    include_package_data=True,
    license='BSD-3 License',
    description="Nine CMS is a simple Django app to manage content.",
    long_description=README,
    url='https://github.com/Wtower/django-ninecms/',
    author='George Karakostas',
    author_email='info@9-dev.com',
    install_requires=[
        'Django',
        'django-guardian',
        'django-mptt',
        'bleach',
        'Pillow',
        'pytz',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD-3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
