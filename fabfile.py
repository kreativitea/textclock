import sys
from fabric.api import env, task, local

env.ve_directory = 'env'


class venv(object):
    def __enter__(self):
        if sys.platform == 'win32':
            local(r'{}\Scripts\activate'.format(env.ve_directory))
        else:
            local(r'{}/bin/activate'.format(env.ve_directory))

    def __exit__(self, _type, value, traceback):
        if sys.platform == 'win32':
            local(r'{}\Scripts\deactivate'.format(env.ve_directory))
        else:
            local(r'{}/bin/deactivate'.format(env.ve_directory))

@task
def bootstrap():
    local('rm -rf {}'.format(env.ve_directory))
    local('virtualenv {}'.format(env.ve_directory))

@task
def setup():
    bootstrap()
    with venv():
        local('pip install -r requirements.txt')

@task
def runserver():
    with venv():
        local('python clockserver.py')
