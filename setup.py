from setuptools import setup, find_packages


setup(
    name='liara-cloud',
    version='1.0.0',
    author='AmirAli Irvany',
    author_email='irvanyamirali@gmail.com',
    description=(
        'Unofficial library for account management and services in Liara Cloud'
    ),
    keywords=['liara', 'liara-cloud', 'session'],
    long_description=open('README.md', encoding='UTF-8').read(),
    python_requires="~=3.7",
    long_description_content_type='text/markdown',
    url='https://github.com/irvanyamirali/liara',
    packages=find_packages(),
    exclude_package_data={
        '': ['*.pyc', '*__pycache__*']
    },
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
