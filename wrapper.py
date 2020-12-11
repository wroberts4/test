from git import Repo
import pip


repo = Repo('./')
repo.git.checkout('v1')
pip.main(['install', '.'])


class main():
    def __init__(self):
        print('version 1')
