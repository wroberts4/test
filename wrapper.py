from git import Repo
import pip
from sys import argv


def version(v):
    repo = Repo('.')
    repo.git.checkout(v)
    pip.main(['install', '.'])

    from main import main
    main()

