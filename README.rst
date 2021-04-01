========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pytemplate/badge/?style=flat
    :target: https://pytemplate.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/jpardovega/pytemplate.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/jpardovega/pytemplate

.. .. |requires| image:: https://requires.io/github/jpardovega/pytemplate/requirements.svg?branch=master
..     :alt: Requirements Status
..     :target: https://requires.io/github/jpardovega/pytemplate/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/jpardovega/pytemplate/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/jpardovega/pytemplate

.. |version| image:: https://img.shields.io/pypi/v/pytemplate.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pytemplate

.. |wheel| image:: https://img.shields.io/pypi/wheel/pytemplate.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pytemplate

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pytemplate.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pytemplate

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pytemplate.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pytemplate

.. |commits-since| image:: https://img.shields.io/github/commits-since/jpardovega/pytemplate/v0.1.2.svg
    :alt: Commits since latest release
    :target: https://github.com/jpardovega/pytemplate/compare/v0.0.0...master



.. end-badges

This is a template for python package using cookiecutter-pylibrary

Installation
============

::

    pip install pytemplate

You can also install the in-development version with::

    pip install https://github.com/jpardovega/pytemplate/archive/master.zip


Documentation
=============


https://pytemplate.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
