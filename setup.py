import os
from distutils.core import setup

#create home directory
if not os.isdir(os.path.join(os.environ['HOME'],'.hissw')):
    os.mkdir(os.path.join(os.environ['HOME'],'.hissw'))

setup(
    name='hissw',
    version='1.0dev',
    author='Will Barnes',
    url='https://github.com/wtbarnes/hissw',
    packages=['hissw']
)