from setuptools import setup


README_FILE = open('README')
try:
        LONG_DESCRIPTION = README_FILE.read()
finally:
        README_FILE.close()


STARTPROJECT_DATA = []

setup(name="djdocker-startproject",
        version="0.1",
        author="Alok Kumar",
        author_email="rajalokan@gmail.com",
        description="Creates a Django project layout for dockerized environment",
        long_description=LONG_DESCRIPTION,
        packages=['djdocker_startproject'],
        package_data={'django_startproject': STARTPROJECT_DATA},
        scripts=['bin/djdocker-startproject.py'],
        classifiers=[
            'Development Status :: Beta',
            'Environment :: Web Environemnt',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
