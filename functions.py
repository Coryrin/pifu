import os


def env(name: str) -> str:
    with open('.env', 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            if key == name:
                return value


def change_directory(directory: str):
    os.chdir(directory)
