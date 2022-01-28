from setuptools import find_packages
from setuptools import setup

version = '0.0.1'

install_requires = [
    'setuptools>=39.0.1',
    'flask',
    'sqlalchemy[asyncio]',
    'nextcord',
]

extras_require = [
    'uvloop;platform_system=="Linux"',
]

setup(
    name='OSDB',
    version=version,
    description='Discord Bot for Old-Shoe discord channel',
    url='https://',
    author='Leonid Kuzin',
    author_email='dg.inc.lcf@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Flask',
        'Topic :: System :: Networking',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    #package_dir={'osdb': 'src/osdb'},
    )
