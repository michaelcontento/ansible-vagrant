#!/usr/bin/env python

from distutils.core import setup

setup(name='ansible-vagrant',
      version='1.0.0',
      description='Simple helper to use ansible with vagrant',
      author='Michael Contento',
      author_email='michaelcontento@gmail.com',
      license='GPLv3',
      install_requires=['ansible'],
      scripts=[
          'bin/ansible-vagrant-update-hosts',
          'bin/ansible-playbook-vagrant',
          'bin/ansible-playbookv',
          'bin/ansible-vagrant',
          'bin/ansiblev',
      ]
)
