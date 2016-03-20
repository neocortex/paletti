import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

BASEDIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
README = os.path.join(BASEDIR, 'README.md')
VERSION = '0.0.1'


setup(
    name='paletti',
    version=VERSION,
    description='Automatic color palette extraction from images',
    long_description=open(README).read(),
    author='Rafael Schultze-Kraft',
    author_email='skraftr@gmail.com',
    url='http://github.com/neocortex/paletti',
    license='MIT',
    packages=['paletti'],
    zip_safe=False,
    install_requires=[
        'colorama',
        'colorific',
        'networkx',
        'numpy',
        'prettytable',
        'requests',
        'scikit-learn',
        'scipy',
    ],
    entry_points={'console_scripts': ['paletti = paletti.run:main']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
)
