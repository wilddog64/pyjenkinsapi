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
    def password():
        return None

    @password.setter
    def password(value):
        self._password = value

    @property
    def config_file_path():
        return config_file_path

    @config_file_path.setter
    def config_file_path(value):
        self._config_file_path = value

    @property
    def config_file():
        return self._config_file

    @config_file.setter
    def config_file(value):
        self._config_file = value

    @property
    def section():
        return self._section

    @section.setter
    def section(value):
        self._section = section

if __name__ == '__main__':
    import jenkinsapi.core
    config_file = 'jenkins.ini'
    jenkins = jenkinsapi.core.Jenkins(config_file=config_file, section='lcjenkins')
    print('jenkins url: %s' % jenkins.url)
    print('jenkins user: %s' % jenkins.user)
