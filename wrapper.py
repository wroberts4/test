from git import Repo
import pip
from sys import argv


def version():
    print('version 2')
    repo = Repo('.')
    repo.git.checkout(string(argv[1]))
    pip.main(['install', '.'])

