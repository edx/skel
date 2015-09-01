"""Set up for {{cookiecutter.project_name}}"""
from setuptools import setup, find_packages

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = '{{cookiecutter.project_name}}/_version.py'
versioneer.versionfile_build = '{{cookiecutter.project_name}}/_version.py'
versioneer.tag_prefix = '{{cookiecutter.project_name}}-'  # tags are like 1.2.0
versioneer.parentdir_prefix = '{{cookiecutter.project_name}}-'  # dirname like 'myproject-1.2.0'

setup(
    name='{{cookiecutter.project_name}}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='{{cookiecutter.project_name}}',
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your requirements here
    ],
    license='{{cookiecutter.license}}',
    classifiers=(
        {% for item in cookiecutter.license_classifiers %}
            "{{item}}",
        {% endfor %}
    )
)
