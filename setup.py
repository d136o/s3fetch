from distutils.core import setup

setup(name='s3QuickTools',
      version='0.0.1-alpha',
      author='Diego Vargas',
      author_email='dvargas@auriq.com',
      url='https://github.com/auriq/s3fetch',
      py_modules=['s3QuickTools'],
      requires=['boto','boto.s3.connection','boto.s3.key'])

      

