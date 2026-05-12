"""
This module contains the tool of collective.recipe.plonesite
"""
from pathlib import Path

from setuptools import find_namespace_packages
from setuptools import setup


def read(*rnames):
    return Path(__file__).parent.joinpath(*rnames).read_text(encoding="utf-8")


version = '2.0.0.dev0'

long_description = (
    f"{read('README.rst')}\n"
    "Detailed Documentation\n"
    "**********************\n"
    f"\n{read('src', 'collective', 'recipe', 'plonesite', 'README.rst')}\n"
    "Contributors\n"
    "************\n"
    f"\n{read('CONTRIBUTORS.rst')}\n"
    "Change history\n"
    "**************\n"
    f"\n{read('CHANGES.rst')}\n"
    "Download\n"
    "********\n"
)

entry_point = 'collective.recipe.plonesite:Recipe'
entry_points = {"zc.buildout": [f"default = {entry_point}"]}

tests_require = ['zope.testing', 'zc.buildout']

setup(
    name='collective.recipe.plonesite',
    version=version,
    description="A buildout recipe to create and update a plone site",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    classifiers=[
        'Framework :: Buildout',
        'Framework :: Plone',
        'Framework :: Plone :: 6.1',
        'Framework :: Plone :: 6.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone buildout recipe',
    author='Clayton Parker',
    author_email='info@sixfeetup.com',
    url='https://github.com/collective/collective.recipe.plonesite',
    license='ZPL',
    packages=find_namespace_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.10',
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    tests_require=tests_require,
    extras_require=dict(
        tests=tests_require,
        upgrade=['collective.upgrade>=1.0rc1'],
    ),
    test_suite='collective.recipe.plonesite.tests.test_docs.test_suite',
    entry_points=entry_points,
)
