from setuptools import setup

setup(
    name='vdmcli',
    version='0.1',
    py_modules=['vdmcli'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        vdmclio=vdmcli:cli
    ''',
)
