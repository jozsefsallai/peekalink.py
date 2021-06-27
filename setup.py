from setuptools import setup

with open('requirements.txt', 'r') as f:
  requirements = f.readlines()

with open('README.md', 'r') as f:
  long_description = f.read()

packages = [
  'peekalink',
  'peekalink.apis',
  'peekalink.models',
  'peekalink.models.helpers'
]

setup(
  name = 'peekalink',
  version = '1.0.0',
  author = 'József Sallai',
  author_email = 'jozsef@sallai.me',
  description = 'A Peekalink API wrapper for Python',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/jozsefsallai/peekalink.py',
  project_urls = {
    'Bug Tracker': 'https://github.com/jozsefsallai/peekalink.py/issues'
  },
  packages = packages,
  include_package_data = True,
  install_requires = requirements,
  python_requires = '>=3.8.0',
  classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities'
  ]
)
