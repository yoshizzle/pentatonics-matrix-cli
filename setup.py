from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pentatonics-matrix-cli',
      version='0.1.0',
      description='A Command Line Interface for penatonic scales',
      long_description=readme(),
      url='http://github.com/yoshizzle/pentatonics-matrix-cli',
      author='Josh Sager',
      author_email='js1@joshsager.com',
      license='MIT',
      packages=['pentatonics-matrix-cli'],
      install_requires=['texttable'],
      zip_safe=False)
