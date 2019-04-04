from os.path import join, dirname
from setuptools import setup


def read(file_name):
    with open(join(dirname(__file__), file_name), encoding='utf-8') as f:
        return f.read()


setup(
    name='pycronius',
    packages=['pycronius'],
    version='0.0.2',
    license='MIT',
    description='It is a fully-tested, benchmarked utility for efficiently matching datetime objects and cron rules.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='The Megawatt Hour',
    author_email='admin@themwh.com',
    url='https://github.com/themwh/pycronius',
    download_url='https://github.com/themwh/pycronius/archive/v0.0.2.tar.gz',
    keywords=['python', 'cron', 'date', 'time', 'match', 'rule'],
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
