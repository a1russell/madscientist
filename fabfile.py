from django.conf import settings
from fabric.api import *


env.hosts = ['adam@madscientist.is-a-geek.net:62000',]
env.project_root = '/usr/local/webapps/'


def deploy():
    """\
    Deploy the latest version of the site to the servers.
    
    """
    # Options for specifying env requirements:
    # Command line, per task: fab deploy:hosts="host1;host2"
    # Command line, globally: fab --hosts host1,host2 deploy
    require('hosts')
    require('project_root')
    import time
    env.release = time.strftime('%Y%m%d%H%M%S')
    local('hg archive --type tgz /tmp/madscientist-%(release)s.tar.gz' % env)
    put('/tmp/madscientist-%(release)s.tar.gz' % env,
        '/tmp/madscientist-%(release)s.tar.gz' % env)
    with cd(env.project_root):
        sudo('tar -xzf /tmp/madscientist-%(release)s.tar.gz' % env)
    sudo('if [[ -d %(project_root)s/madscientist ]]; then '
         'mv %(project_root)s/madscientist '
         '%(project_root)s/madscientist-%(release)s.bak;'
         'fi' % env)
    sudo('mv %(project_root)s/madscientist-%(release)s '
         '%(project_root)s/madscientist' % env)
    sudo('if [[ -d %(project_root)s/madscientist-%(release)s.bak ]]; then '
         'mv %(project_root)s/madscientist-%(release)s.bak/settings_local.py '
         '%(project_root)s/madscientist/;'
         'rm -rf %(project_root)s/madscientist-%(release)s.bak;'
         'fi' % env)
    sudo('chown -R root:www-admin %(project_root)s/madscientist' % env)
    sudo('chmod -R g+w %(project_root)s/madscientist' % env)
    run('rm /tmp/madscientist-%(release)s.tar.gz' % env)
    local('rm /tmp/madscientist-%(release)s.tar.gz' % env)
    sudo('apache2ctl -k graceful')

