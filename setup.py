#!/usr/bin/env python3

from setuptools import setup

setup(name='uptime-consumer',
      version='1.0.0',
      description='Kafka consumer that stores received uptime data on PostgeSQL',
      author='Felipe Morato',
      author_email='me@fmorato.com',
      url='https://fmorato.com/',
      download_url='https://github.com/fmorato/uptime-consumer.git',
      keywords='kafka consumer postgresql',
      scripts=[
          'consumer',
          'setup-postgres'
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: No Input/Output (Daemon)',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: Implementation :: CPython',
      ],
      license='GPL-3',
      python_requires='>=3.5',
      install_requires=[
          'kafka-python',
          'psycopg2-binary'
      ],
      )
