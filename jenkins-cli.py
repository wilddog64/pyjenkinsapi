import click
import jenkinsapi.core
from jenkinsapi.config.core import config_section_map

@click.group()
@click.option('-c', '--config-path', help='jenkins-cli configuration path', default='')
@click.option('--section-name', help='section in jenkins-cli configuration file', default='lcjenkins')
@click.option('-s', '--jenkins-server-url', help='jenkins server url', default='')
@click.option('-u', '--jenkins-user', help='jenkins user name', default='')
@click.option('-p', '--jenkins-password', help='jenkins user password', default='')
@click.pass_context
def jenkins(ctx, jenkins_server_url, config_path, section_name, jenkins_user, jenkins_password):
    jenkins_config = config_section_map(config_file='jenkins.ini',
                                        config_file_path=config_path,
                                        section_name='lcjenkins')
    jenkins_user = jenkins_config['user'] if jenkins_user == '' else jenkins_user
    jenkins_password = jenkins_config['password'] if jenkins_password == '' else jenkins_password
    jenkins_server_url = jenkins_config['url'] if jenkins_server_url == '' else jenkins_server_url
    ctx.meta['jenkins'] = jenkinsapi.core.Jenkins(jenkins_server_url, jenkins_user, jenkins_password)

@jenkins.command('views')
def views():
    click.echo('a list of jenkins view')

@jenkins.command('jobs')
def jobs():
    click.echo('list all jobs from a given jenkins servers')


if __name__ == '__main__':
    jenkins()
