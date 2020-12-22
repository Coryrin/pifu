from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

import json
import os
from functions import *

PROJECT_DIR = 'C:\\Users\\Coryr\\Documents\\projects'
def start_project(project, title):
    project = project.lower()

    with open("start_project/project_commands.json") as json_file:
        projects = json.load(json_file)
        command = ''
        for item in projects:
            if item['project'] == project:
                command = item['command']
                break
        
        change_directory(PROJECT_DIR)
        os.system(command.format(title))
        os.system("code .")
    
if __name__ == '__main__':
    start_project("django", "my_project")
