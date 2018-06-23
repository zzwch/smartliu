from setuptools import setup

setup(
    name='smartliu',
    version='0.3',
    py_modules=['smartliu'],
    install_requires=[
        'Click',
        'biopython',
    ],
    entry_points='''
        [console_scripts]
        smartliu=smartliu:smart
    ''',
)
