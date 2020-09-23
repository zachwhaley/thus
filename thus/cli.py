# -*- coding: utf-8 -*-

import click
from dataclasses import dataclass

import DeepSecurity
import SmartCheck
import CloudConformity
import logging

from session import Session
LOG = logging.getLogger('thus.cli')
LOG_FORMAT = ('%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')

# Don't remove this line.  The idna encoding
# is used by getaddrinfo when dealing with unicode hostnames,
# and in some cases, there appears to be a race condition
# where threads will get a LookupError on getaddrinfo() saying
# that the encoding doesn't exist.  Using the idna encoding before
# running any CLI code (and any threads it may create) ensures that
# the encodings.idna is imported and registered in the codecs registry,
# which will stop the LookupErrors from happening.
# See: https://bugs.python.org/issue29288
u''.encode('idna')

def _set_user_agent_for_session(session):
    session.user_agent_name = 'thus-cli'

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
        if aliases[cmd_name] not in self.list_commands(ctx):
            return None
        return click.Group.get_command(self, ctx, aliases[cmd_name])

def findclass(module, command):
    listing = dir (module)
    for c in listing:
        if c.lower() == command.lower():
            command = c
            break
    classToCall = getattr(module, command)
    return classToCall

def findfunction(rtv, subcommand):
    listing = dir(rtv)
    for f in listing:
        if f.lower() == subcommand.lower():
            subcommand = f
            break
    method_to_call = getattr(rtv, subcommand)
    return method_to_call

@click.command(cls=AliasedGroup)
@click.option('--profile', help='AWS profile name')
@click.pass_context
def thus(ctx, profile):
    ctx.obj.profile = profile


@click.command(short_help='alias: cc')
@click.argument('subcommand')
@click.argument('arguments', nargs=-1)
@click.pass_context
def cloudconformity(ctx, subcommand, arguments):
    config = ctx.obj.session.BuildCCConfig(profile=ctx.obj.profile)
    connection = CloudConformity.connect.Connection(config=config)
    group_to_call = findclass(module=CloudConformity, command=ctx.command.name)
    rtv = group_to_call(config=config, connection=connection)
    method_to_call = findfunction(rtv, subcommand)
    rtv = method_to_call(*arguments)


#@click.command(short_help='alias: ws')
#def workloadsecurity():
#    click.echo('workloadsecurity')
#
#
#@click.command(short_help='alias: cs')
#def containersecurity():
#    click.echo('containersecurity')
#
#@click.command(short_help='alias: ds')
#def deepsecurity():
#    click.echo('deepsecurity')
#
#
#@click.command(short_help='alias: sc')
#def smartcheck():
#    click.echo('smartcheck')

thus.add_command(cloudconformity)
#thus.add_command(workloadsecurity)
#thus.add_command(containersecurity)
#thus.add_command(deepsecurity)
#thus.add_command(smartcheck)

@dataclass
class CliObj:
    session: Session
    profile: str = None

if __name__ == '__main__':
    session =  Session()
    _set_user_agent_for_session(session)
    thus(obj=CliObj(session))
