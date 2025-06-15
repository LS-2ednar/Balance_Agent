import os

def run_python_file(working_directory, file_path):
    cwd = os.path.abspath(working_directory)
    wd = os.path.abspath(os.path.join(working_directory, file_path))

    if not wd.startswith(cwd):
        f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

   
