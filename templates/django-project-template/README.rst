{% if False %}
Installation
------------

To start a new project with this template::

    django-admin.py startproject --template=https://github.com/edx/django-project-template/zipball/master --extension=py,rst,yml,gitignore  --name=Makefile <project_name>
    django-admin.py startproject --template=~/workspace/django-project-template --extension=py,rst,yml,gitignore --name=Makefile <project_name>

{% endif %}
{{ project_name }}  |Travis|_ |Coveralls|_
==========================================
.. |Travis| image:: https://travis-ci.org/edx/{{ project_name }}.svg?branch=master
.. _Travis: https://travis-ci.org/edx/{{ project_name }}

.. |Coveralls| image:: https://coveralls.io/repos/edx/{{ project_name }}/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/r/edx/{{ project_name }}?branch=master

INSERT A BRIEF DESCRIPTION OF THE PROJECT HERE.

Prerequisites
-------------
* Python 2.7.x (not tested with Python 3.x)
* `gettext <http://www.gnu.org/software/gettext/>`_
* `npm <https://www.npmjs.org/>`_


# TODO: Basic installation instructions
# TODO: Asset compilation
# TODO: Testing
# TODO: Licensing
# TODO: OpenEdX contributions
