from setuptools import setup

setup(
    name='vdmcli',
    version='0.1',
    py_modules=['vdmcli'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        vdmcli=vdmcli:cli
    ''',
)
