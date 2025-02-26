from setuptools import setup


LGTV_VERSION = '0.3'
LGTV_DOWNLOAD_URL = (
    'https://github.com/ShaimaaHamd26/LGWebOSRemote/tarball/' + LGTV_VERSION
)

setup(
    name='LGTV',
    packages=['LGTV'],
    version=LGTV_VERSION,
    description='LG WebOS TV Controller.',
    long_description='',
    license='MIT',
    author='Karl Lattimer',
    author_email='karl@qdh.org.uk',
    url='https://github.com/ShaimaaHamd26/LGWebOSRemote',
    download_url=LGTV_DOWNLOAD_URL,
    entry_points={
        'console_scripts': [
            'lgtv=LGTV:main'
        ]
    },
    keywords=[
        'smarthome', 'smarttv', 'lg', 'tv', 'webos', 'remote'
    ],
    install_requires=[
        'wakeonlan',
        'ws4py',
        'requests',
        'getmac',
    ],
    data_files=[
        ('config', ['data/config.json'])
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
    ],
)
