#!/usr/bin/env python

from distutils.core import setup

setup(name="modules-logger",
      version='0.2',
      description="Log usage of environment-modules to MongoDB",
      author="Adam DeConinck",
      author_email="ajdecon@ajdecon.org",
      url="https://github.com/ajdecon/modules_logger",
      scripts=["modules_logger","modules_usage","modules_stats"],
      data_files=[('/etc/',["modules_logger.conf"]),
                  ('/etc/profile.d/',['modules.sh.logger']),
                  ('/usr/share/man/man1/',['man/modules_logger.1','man/modules_usage.1']),
                  ('/usr/share/man/man5/',['man/modules_logger.5'])
                  ],
      license="Apache 2.0",
      requires=["pymongo","ConfigParser"])
