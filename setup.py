#!/usr/bin/env python

from distutils.core import setup

import pypandoc


setup(name='ansible-vagrant',
      version='1.1.0',
      description='Simple helper to use ansible with vagrant',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='https://github.com/michaelcontento/ansible-vagrant',
      author='Michael Contento',
      author_email='michaelcontento@gmail.com',
      license='GPLv3',
      install_requires=['ansible'],
      keywords=['vagrant', 'ansible'],
      scripts=[
          'bin/ansible-vagrant-update-hosts',
          'bin/ansible-playbook-vagrant',
          'bin/ansible-playbookv',
          'bin/ansible-vagrant',
          'bin/ansiblev',
      ],
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: System :: Clustering',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities'
      ],
)
