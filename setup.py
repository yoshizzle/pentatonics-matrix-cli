from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pentatonics-matrix-cli',
      version='0.1.2',
      description='A Command Line Interface for penatonic scales',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education :: Music',
        'Natural Language:: English',
        'Intended Audience:: Other Audience',
      ],
      url='http://github.com/yoshizzle/pentatonics-matrix-cli',
      author='Josh Sager',
      author_email='js1@joshsager.com',
      license='MIT',
      packages=['pentatonics-matrix-cli'],
      install_requires=['texttable'],
      zip_safe=False)
