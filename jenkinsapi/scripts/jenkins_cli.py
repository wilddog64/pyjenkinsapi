import click
import jenkinsapi.core
from jenkinsapi.config.core import config_section_map
from functools import update_wrapper

@click.group(chain=True)
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

@cli.resultcallback()
def process_commands(processors):
    """This result callback is invoked with an iterable of all the chained
    subcommands.  As in this example each subcommand returns a function
    we can chain them together to feed one into the other, similar to how
    a pipe on unix works.
    """
    # Start with an empty iterable.
    stream = ()

    # Pipe it through all stream processors.
    for processor in processors:
        stream = processor(stream)

    # Evaluate the stream and throw away the items.
    for _ in stream:
        pass


def processor(f):
    """Helper decorator to rewrite a function so that it returns another
    function from it.
    """
    def new_func(*args, **kwargs):
        def processor(stream):
            return f(stream, *args, **kwargs)
        return processor
    return update_wrapper(new_func, f)


def generator(f):
    """Similar to the :func:`processor` but passes through old values
    unchanged and does not pass through the values as parameter.
    """
    @processor
    def new_func(stream, *args, **kwargs):
        for item in stream:
            yield item
        for item in f(*args, **kwargs):
            yield item
    return update_wrapper(new_func, f)

if __name__ == '__main__':
    jenkins()
