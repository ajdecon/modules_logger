#!/usr/bin/env python

from distutils.core import setup

setup(name="modules-logger",
      version='0.1',
      description="Log usage of environment-modules to MongoDB",
      author="Adam DeConinck",
      author_email="ajdecon@ajdecon.org",
      url="https://github.com/ajdecon/modules_logger",
      scripts=["modules_logger","modules_usage"],
      data_files=[('/etc/',["modules_logger.conf"]),
                  ('/etc/profile.d/',['modules.sh.logger'])],
      license="Apache 2.0",
      requires=["pymongo","ConfigParser"])
