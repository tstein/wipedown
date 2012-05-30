from setuptools import setup

import wipedown


setup(
    name = 'wipedown',
    packages = ['wipedown'],
    description = 'Generate passwords that are resistant to smudge attacks.',
    version = wipedown.__version__,
    author = 'Ted Stein',
    author_email = 'karamarisan@gmail.com',
    entry_points = {
      'console_scripts': [
        'wipedown = wipedown:entry'
      ]
    }
)

