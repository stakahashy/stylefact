from setuptools import setup, find_packages
from codecs import open
from os import path
import re

from stylefact._version import __author__ as author
from stylefact._version import __author_email__ as author_email
from stylefact._version import __copyright__ as copyright
from stylefact._version import __description__ as description
from stylefact._version import __docs_copyright__ as docs_copyright
from stylefact._version import __license__ as license
from stylefact._version import __title__ as title
from stylefact._version import __url__ as url
from stylefact._version import __version__ as version

with open('README.md',encoding='utf-8') as f:
    long_description = f.read()
long_description = ''
root_dir = path.abspath(path.dirname(__file__))

def requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]


def test_requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]

package_name = 'stylefact'

setup(name=package_name,
        packages=[package_name],
        version=version,
        license=license,
        install_requires=requirements(),
        tests_require=test_requirements(),
        author=author,
        author_email=author_email,
        url=url,
        description="Toolkit for stylized facts",
        long_description=long_description,
        keywords="stylized facts, econophysics, finance",
        classifiers=['Development Status :: 5 - Production/Stable',"Programming Language :: Python","Programming Language :: Python :: 3"],
        long_description_content_type='text/markdown')
