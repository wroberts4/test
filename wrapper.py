from git import Repo
import pip
from sys import argv


def version(v):
    print('version 2')
    repo = Repo('.')
    repo.git.checkout(v)
    pip.main(['install', '.'])

