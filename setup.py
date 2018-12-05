DESCRIPTION = "A python package for heart rate variability analysis"
DISTNAME = 'hrv'
MAINTAINER = 'Rhenan Bartels'
MAINTAINER_EMAIL = 'rhenan.bartels@gmail.com'
URL = 'https://github.com/rhenanbartels/hrv'
LICENSE = 'BSD'
DOWNLOAD_URL = 'https://github.com/rhenanbartels/hrv'
INSTALL_REQUIRES = ['numpy', 'scipy', 'spectrum']
VERSION = '0.1.5'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

if __name__ == "__main__":

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=INSTALL_REQUIRES,
          include_package_data=True,
          packages=['hrv'],
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 3.6',
              'License :: OSI Approved :: BSD License',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
          )
