# -* - coding: UTF-8 -* -
import os
import subprocess


class Bcat(object):
    """docstring for Bcat"""

    def __init__(self, version, config):
        super(Bcat, self).__init__()

        self.version = version
        self.url = config['BCAT_GIT_URL']

    def get_source(self):
        cmd = "git clone " + self.url
        result = subprocess.call(cmd, shell=True)
        return result

    def git_pull(self):
        cmd = "git pull"
        result = subprocess.call(cmd, shell=True, cwd="./bcat")
        return result

    def git_reset(self, version=None):
        if version == None:
            head = "git reflog --pretty=oneline | awk -F ' ' 'NR==1 {print $1}'"
            cmd = "git reset --hard `{0}`".format(head)
        else:
            cmd = "git checkout {0}".format(version)
        # print cmd
        p = subprocess.Popen(cmd, shell=True, cwd="./bcat")
        sts = os.waitpid(p.pid, 0)[1]
        return sts


if __name__ == '__main__':
    # bcat = Bcat("test", "config")
    # bcat.get_source()
    # bcat.git_pull()
    # bcat.git_reset()
