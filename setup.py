from setuptools import setup, find_packages

setup(
    name='livedownload',
    keywords=['LiveDownload', 'bilibili'],
    license='GNU General Public License v3',
    description='',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/LiveDownload/LiveDownload',
    python_requires='>=3.6',
    install_requires=[
        'Click>=7.0',
        'aiohttp>=3.6.2, <4.0',
        'colorlog>=4.1.0',
        'dataclasses>=0.7'
    ],
    entry_points={
        'console_scripts': [
            'livedownload=livedownload.main:main',
        ],
    },
    zip_safe=False
)
