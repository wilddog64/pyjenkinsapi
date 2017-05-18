from setuptools import setup, find_packages
setup(
    name='jenkinsapi',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        jenkins-cli=jenkinsapi.scripts.jenkins_cli:jenkins
    ''',
)
