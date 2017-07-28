from setuptools import setup, find_packages
setup(
    name='jenkinsapi',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pathlib2'
    ],
    entry_points='''
        [console_scripts]
        jenkins-cmd=jenkinsapi.scripts.jenkins_cli:jenkins
    ''',
)
