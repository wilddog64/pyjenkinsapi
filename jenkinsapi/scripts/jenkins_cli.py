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
    ctx.obj = jenkinsapi.core.Jenkins(jenkins_server_url, jenkins_user, jenkins_password)

@jenkins.command('views')
@click.option('-a', '--all', type=click.BOOL, is_flag=True, help='list all or a particular view', default=False)
@click.option('-j', '--jobs', type=click.BOOL, is_flag=True, help='list jobs for views', default=False)
@click.argument('names', nargs=-1)
@click.pass_obj
def views(jenkins, all, jobs, names):
    if all:
        click.echo(jenkins.views)
    else:
        if names:
            for name in names:
                click.echo('view %s has these jobs:' % name)
                click.echo('=======================')
                jobs = [job.name for job in jenkins.views[name].jobs]
                print("\n".join(jobs))
                print('')

@jenkins.command('jobs')
def jobs():
    click.echo('list all jobs from a given jenkins servers')

if __name__ == '__main__':
    jenkins()