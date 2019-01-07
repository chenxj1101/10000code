from setuptools import setup


setup(
    name='unp',
    py_modules=['unp'],
    install_requires=[
        'click>=3.0',
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    entry_points='''
        [console_scripts]
        unp=unp:cli
    ''',
)