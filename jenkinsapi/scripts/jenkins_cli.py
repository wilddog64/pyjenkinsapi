import click
import jenkinsapi.core
import os
from pathlib2 import Path
from jenkinsapi.config.core import config_section_map

@click.group()
@click.option('-c', '--config-path', help='jenkins-cli configuration path', default='')
@click.option('--section-name', help='section in jenkins-cli configuration file', default='')
@click.option('-s', '--jenkins-server-url', help='jenkins server url', default='')
@click.option('-u', '--jenkins-user', help='jenkins user name', default='')
@click.option('-p', '--jenkins-password', help='jenkins user password', default='')
@click.pass_context
def jenkins(ctx, jenkins_server_url, config_path, section_name, jenkins_user, jenkins_password):
    jenkins_config = None
    if not section_name == '':
        jenkins_config = config_section_map(config_file='jenkins.ini',
                                            config_file_path=config_path,
                                            section_name='lcjenkins')
    # let's see if there're any environment variables defined
    environ = os.environ
    jenkins_user = environ['JENKINS_USER'] if 'JENKINS_USER' in environ else ''
    jenkins_password = environ['JENKINS_API_TOKEN'] if 'JENKINS_API_TOKEN' in environ['JENKINS_API_TOKEN'] else ''
    jenkins_server_url = environ['JENKINS_URL'] if 'JENKINS_URL' in environ['JENKINS_URL'] else ''

    if jenkins_config:
        jenkins_user = jenkins_config['user'] if jenkins_user == '' else jenkins_user
        jenkins_password = jenkins_config['password'] if jenkins_password == '' else jenkins_password
        jenkins_server_url = jenkins_config['url'] if jenkins_server_url == '' else jenkins_server_url

    ctx.obj = jenkinsapi.core.Jenkins(jenkins_server_url, jenkins_user, jenkins_password)

@jenkins.command('views')
@click.option('-a', '--all', type=click.BOOL, is_flag=True, help='list all or a particular view', default=False)
@click.option('-j', '--jobs', type=click.BOOL, is_flag=True, help='list jobs for views', default='/tmp/jenkins')
@click.option('--save-all-jobs', type=click.BOOL, is_flag=True, help='save all jobs')
@click.option('--save-job', help='save a particular job for this view')
@click.option('-p', '--path', help='a path to save job defintions')
@click.argument('names', nargs=-1)
@click.pass_obj
def views(jenkins, all, jobs, save_all_jobs, save_job, path, names):
    save_job = '' if save_job == None else save_job
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

    if save_all_jobs:
        for job in jenkins.views[name].jobs:
            save_job_configs(job, name, path)
    elif save_job != '':
        job = [job.name for job in jenkins.views[name].jobs if job.name == save_job][0]
        if job:
            save_job_configs(job, name, path)


@jenkins.command('jobs')
def jobs():
    click.echo('list all jobs from a given jenkins servers')

def save_job_configs(job, view_name, jobs_dir):
    '''

    '''
    path = os.path.join(jobs_dir, view_name)
    if not is_path_exists(path):
        os.makedirs(path)

    job_config_path = os.path.join(path, "%s.%s" % (job.name, 'xml'))
    click.echo('writing %s to %s' %  (job.name, job_config_path) )
    with open(job_config_path, 'w') as f:
        f.writelines(job.config)


def is_path_exists(directory):
    path = Path(directory)

    return path.exists()

if __name__ == '__main__':
    jenkins()
