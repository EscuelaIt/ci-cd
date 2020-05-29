import os
from fabric.operations import run
from fabric.state import env
from fabric.context_managers import cd
from fabric.api import warn_only


environments = {
    'production': {
        'hosts': os.environ['PRODUCTION_IP'],
        'home': '/var/meetup',
        'docker_commands': [
            'docker-compose -f production.yml build --no-cache',
            'docker-compose -f production.yml down',
            'docker volume rm $(docker volume ls -qf dangling=true)',
            'docker-compose -f production.yml up -d',
        ],
        'git': {
            'parent': 'origin',
            'branch': 'master',
        },
    },
    'beta': {
        'hosts': os.environ['PRODUCTION_IP'],
        'home': '/var/meetup',
        'docker_commands': [
            'docker-compose -f production.yml build --no-cache',
            'docker-compose -f production.yml down',
            'docker volume rm $(docker volume ls -qf dangling=true)',
            'docker-compose -f production.yml up -d',
        ],
        'git': {
            'parent': 'origin',
            'branch': 'master',
        },
    }
}


# setup
def production():
    environments['default'] = environments['production']
    env.hosts = environments['production']['hosts']


def beta():
    environments['default'] = environments['beta']
    env.hosts = environments['beta']['hosts']


def git_pull():
    with cd(environments['default']['home']):
        run('git pull %s %s' % (environments['default']['git']['parent'],
                                environments['default']['git']['branch']))


def docker_commands():
    with warn_only():
        with cd(environments['default']['home']):
            for command in environments['default']['docker_commands']:
                run(command)


def update_cert_commands():
    with cd(environments['default']['home']):
        for command in environments['default']['update_cert_commands']:
            run(command)


def deploy():
    git_pull()
    docker_commands()
