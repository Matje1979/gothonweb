try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = [
    'description': 'My Project',
    'author': 'Damir Cicic',
    'url': 'URL to get it at',
    'download_url': 'Where to download it'.
    'author_email': 'damircicic@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['bin', 'gothonweb']
    'scripts': ["bin\app.py", "gothonweb\map.py"],
    'name': 'projectname'
]

setup(**config)