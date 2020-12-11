from git import Repo
import pip
from sys import argv


def version():
    print('version 1')


if __name__ == 'main':
    repo = Repo('.')
    repo.git.checkout(argv[1])
    pip.main(['install', '.'])
