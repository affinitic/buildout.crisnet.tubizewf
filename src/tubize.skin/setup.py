from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='tubize.skin',
      version=version,
      description="Tubize Skin",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='tubize skin theme affinitic',
      author='Affinitic Sprl',
      author_email='info@affinitic.be',
      url='http://www.amte.be',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tubize'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
