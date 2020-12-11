from git import Repo
import pip
from sys import argv


def version(v):
    print('version 1')
    repo = Repo('.')
    repo.git.checkout(v)
    pip.main(['install', '.'])

