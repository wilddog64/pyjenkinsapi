import click


@click.group()
def jenkins():
    pass

@jenkins.command('views')
def views():
    click.echo('a list of jenkins view')

@jenkins.command('jobs')
def jobs():
    click.echo('list all jobs from a given jenkins servers')


if __name__ == '__main__':
    jenkins()
