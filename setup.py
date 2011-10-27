from distutils.core import setup

setup(
        name='Rangansson',
        version='0.1.0',
        author='Harshavardhan Rangan',
        author_email='hvardhan.r@gmail.com',
        packages=['rangansson', 'rangansson.test'],
        scripts=['bin/rangansson'],
        url='http://www.hrangan.net/rangansson',
        license='LICENSE.txt',
        description='A genealogy package',
        long_description=open('README.txt').read(),
        install_requires=[
            "xml >= 41660",
        ],
)
