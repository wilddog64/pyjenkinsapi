from __future__ import print_function
import jenkinsapi.views
from jenkinsapi.config.core import config_section_map
import jenkins
import urllib3

class Jenkins:
    def __init__(self, url='',
                       user='',
                       password='',
                       verify_ssl=False):


        # if url, user, and password are not empty use them, otherwise, read them
        # if we disable verify ssl then we should also disable_warnings for ssl
        if not self._verify_ssl:
            urllib3.disable_warnings()

        # from configuration file
        self.url = url if url != '' else config_map['url']
        self.user = user if user != '' else config_map['user']
        self._password = password if password != '' else config_map['password']
        self._jenkins = jenkins.Jenkins(self.url, self.user, self._password, self.verify_ssl)
        self._views = jenkinsapi.views.Views()
        for view in self._jenkins.views:
            self._views[view.name] = view

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
        return self._views

    @property
    def verify_ssl(self):
        return self._verify_ssl

if __name__ == '__main__':
    import jenkinsapi.core
    from jenkinsapi.config.core import config_section_map
    config_file = 'jenkins.ini'
    jenkins_config = config_section_map(config_file='jenkins.ini', section_name='lcjenkins')
    jenkins_user = jenkins_config['user']
    jenkins_password = jenkins_config['password']
    jenkins_server_url = jenkins_config['url']

    jenkins = jenkinsapi.core.Jenkins(jenkins_server_url, jenkins_user, jenkins_password)
    print('jenkins url: %s' % jenkins.url)
    print('jenkins user: %s' % jenkins.user)

    # list all the views for a given jenkins server
    for view in jenkins.views:
        print(view)

    print('--- all views ---')
    print(jenkins.views)
    print('')

    # list all the jobs for a given jenkins server
    print('--- all jobs ---')
    for job in jenkins.jobs:
        print(job.name)

    print('')

    print('--- view qa sites job: ---')
    qasites_view = jenkins.views['QA Sites']
    print('view name is %s' % qasites_view.name)
    qasites_jobs = "\n".join(qasites_view.jobnames)
    print('')
    print("--- QA Sites jobs are: ---")
    print(qasites_jobs)
    print('')
