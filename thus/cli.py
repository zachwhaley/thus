# -*- coding: utf-8 -*-

import click

aliases = {
        'cc': 'cloudconformity',
        'ws': 'workloadsecurity',
        'cs': 'containersecurity',
        'ds': 'deepsecurity',
        'sc': 'smartcheck',
        }

class AliasedGroup(click.Group):

    def get_command(self, ctx, cmd_name):
        cmd = click.Group.get_command(self, ctx, cmd_name)
        if cmd is not None:
            return cmd
        if cmd_name not in aliases:
            return None
        if aliases[cmd_name] in self.list_commands(ctx):
            return click.Group.get_command(self, ctx, aliases[cmd_name])
        return None


@click.command(cls=AliasedGroup)
def thus():
    pass


@click.command(short_help='alias: cc')
def cloudconformity():
    click.echo('cloudconformity')


@click.command(short_help='alias: ws')
def workloadsecurity():
    click.echo('workloadsecurity')


@click.command(short_help='alias: cs')
def containersecurity():
    click.echo('containersecurity')

@click.command(short_help='alias: ds')
def deepsecurity():
    click.echo('deepsecurity')


@click.command(short_help='alias: sc')
def smartcheck():
    click.echo('smartcheck')

thus.add_command(cloudconformity)
thus.add_command(workloadsecurity)
thus.add_command(containersecurity)
thus.add_command(deepsecurity)
thus.add_command(smartcheck)

if __name__ == '__main__':
    thus()
