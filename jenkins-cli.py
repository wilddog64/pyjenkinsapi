import click


@click.group()
@click.option('-s', '--server', help='jenkins server url')
def jenkins(server):
    click.echo('jenkins server %s' % server)

@jenkins.command('views')
def views():
    click.echo('a list of jenkins view')

@jenkins.command('jobs')
def jobs():
    click.echo('list all jobs from a given jenkins servers')


if __name__ == '__main__':
    jenkins()
