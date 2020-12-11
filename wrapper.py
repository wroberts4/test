from git import Repo
import pip
from sys import argv
from main import main


def version(v):
    repo = Repo('.')
    repo.git.checkout(v)
    pip.main(['install', '.'])
    main()

