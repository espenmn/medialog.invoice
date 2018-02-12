from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='medialog.invoice',
version=version,
      description="invoice templates for produce and publish",
      long_description=open("README.rst").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=["Framework :: Plone",
          "Framework :: Plone :: 5",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Framework :: Zope2",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='PDF Plone invoice',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/medialog.invoice',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pp.client-plone',
          'medialog.controlpanel'
          # -*- Extra requirements: -*-
      ],
      tests_require=['zope.testing'],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
