import json
import os

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
        
        os.chdir(PROJECT_DIR)
        os.system(command.format(title))
        os.system("code .")
    
if __name__ == '__main__':
    start_project("laravel", "laravel_project")
