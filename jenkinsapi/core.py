from __future__ import print_function
from jenkinsapi.config.core import config_section_map
import jenkins

class Jenkins:
    def __init__(self, url='',
                       user='',
                       password='',
                       config_file_path='',
                       config_file='',
                       section=''):

        # read configuration from jenkins.ini section
        config_map = config_section_map(config_file_path=config_file_path,
                                        config_file=config_file,
                                        section_name=section)

        # if url, user, and password are not empty use them, otherwise, read them
        # from configuration file
        self.url = url if url != '' else config_map['url']
        self.user = user if user != '' else config_map['user']
        self._password = password if password != '' else config_map['password']
        self._jenkins = jenkins.Jenkins(self.url, self.user, self._password)

    @property
    def user():
        return self._user;

    @user.setter
    def user(value):
        self._user = value

    @property
    def url():
        return self._url

    @url.setter
    def url(value):
        self._url = value

    @property
    def config_file_path():
        return config_file_path

    @config_file_path.setter
    def config_file_path(value):
        self._config_file_path = value

    @property
    def config_file(self):
        return self._config_file

    @config_file.setter
    def config_file(value):
        self._config_file = value

    @property
    def section(self):
        return self._section

    @section.setter
    def section(value):
        self._section = section

    @property
    def jenkins(self):
        return self._jenkins

    @property
    def jobs(self):
        return self._jenkins.jobs

    @property
    def views(self):
        return self.jenkins.views

if __name__ == '__main__':
    import jenkinsapi.core
    config_file = 'jenkins.ini'
    jenkins = jenkinsapi.core.Jenkins(config_file=config_file, section='lcjenkins')
    print('jenkins url: %s' % jenkins.url)
    print('jenkins user: %s' % jenkins.user)

    # list all the views for a given jenkins server
    for view in jenkins.views:
        print(view.name)

    # list all the jobs for a given jenkins server
    for job in jenkins.jobs:
        print(job.name)
