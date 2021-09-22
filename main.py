import os
from classes.pifu import Pifu

BASE_DIR = os.getcwd()


def main():
    pifu = Pifu()
    while pifu.listen_to_speech:
        pifu.listen()


def reset_directory():
    os.chdir(BASE_DIR)


if __name__ == '__main__':
    main()
