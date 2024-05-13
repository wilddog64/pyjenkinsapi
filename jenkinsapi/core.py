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
        self._verify_ssl = verify_ssl
        if not self._verify_ssl:
            urllib3.disable_warnings()

        # from configuration file
        self.url = url
        self.user = user
        self._password = password
        self._jenkins = jenkins.Jenkins(self.url, self.user, self._password, self._verify_ssl)
        self._views = jenkinsapi.views.Views()
        for view in self._jenkins.views:
            self._views[view.name] = view

    @property
    def user(self):
        return self._user;

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def config_file_path(self):
        return config_file_path

    @config_file_path.setter
    def config_file_path(self, value):
        self._config_file_path = value

    @property
    def config_file(self):
        return self._config_file

    @config_file.setter
    def config_file(self, value):
        self._config_file = value

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
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

    def build(self, job_name, job_number):
        self.jenkins.build(job_name, job_number)

if __name__ == '__main__':
    import jenkinsapi.core
    import os
    from jenkinsapi.config.core import config_section_map
    # config_file = 'jenkins.ini'
    # jenkins_config = config_section_map(config_file='jenkins.ini', section_name='lcjenkins')

    jenkins_user = ''
    jenkins_password = ''
    jenkins_server_url = ''

    jenkins_user = os.environ['JENKINS_USER']
    jenkins_password = os.environ['JENKINS_USER_PASS']
    jenkins_server_url = os.environ['JENKINS_SERVER_URL']

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

    print('--- view batch sites job: ---')
    batch = jenkins.views['Batch']
    print('view name is %s' % batch.name)
    batch_jobs = "\n".join(batch.jobnames)
    print('')
    print("--- QA Sites jobs are: ---")
    print(batch_jobs)
    print('')
