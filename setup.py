from setuptools import setup

setup(name='musicdata',
      version='0.1',
      description='Python package allowing easy access to music data from major music websites.',
      url='http://github.com/renothiart/MusicData',
      author='Reno Thiart',
      author_email='rthiart@seas.upenn.edu',
      license='MIT',
      packages=['musicdata'],
      install_requires=[
      	"requests",
      	"bs4"
      ],
      zip_safe=False)