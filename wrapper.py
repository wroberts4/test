from git import Repo
import pip
from sys import argv
from importlib import reload
import main


def version(v):
    repo = Repo('.')
    repo.git.checkout(v)
    pip.main(['install', '.'])

    reload(main)
    main.main()

