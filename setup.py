VERSION = '0,1,4'
import os
from setuptools import setup, find_packages,findall
from glob import glob

def get_version():
    l,m,s = VERSION.split(',')
    return '{}.{}.{}'.format(l,m,s).strip()

make_file = lambda dn,f: os.path.join(os.curdir,os.sep,dn,f)

def get_pkg_data():
    data = os.walk(os.path.dirname(__file__))
    pkg_data = []

    for dn,dl,fl in data:
        if 'templates' in dn.split('/'):
            for f in fl:
                if not f.endswith('.py'):
                    pkg_data.append(make_file(dn,f))
    return pkg_data

config = dict(
        name='flask-macros',
        version=get_version(),
        include_package_data=True,
        author='Kyle Roux',
        author_email='kyle@level2designs.com',
        description='macros for flask projects',
        long_description='',
        packages=['flask_macros'],
        package_data = {'':findall('flask_macros')},     #['*.bob','*.html','*.js','*.css','*',]},
        install_requires=[
            'flask==0.10.1',
            'jinja2==2.7.3',
            'WTForms==2.0.1',
            ],
        zip_safe=False,
)

if __name__ == "__main__":
    setup(**config)
