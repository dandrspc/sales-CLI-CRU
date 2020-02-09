from setuptools import setup


setup(
    name='sales',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sales=pv:cli
    ''',
)
