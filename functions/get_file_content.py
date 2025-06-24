from config import MAX_CHARS
import os

def get_file_content(working_directory, file_path):
    
    cwd= os.path.abspath(working_directory)
    wd = os.path.abspath(os.path.join(working_directory,file_path))

    if not wd.startswith(cwd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(wd):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(wd,"r") as ft:
            file_content_string = ft.read(MAX_CHARS)

        if len(file_content_string) == MAX_CHARS:
            return f'{file_content_string} "{file_path}" truncated at 10000 characters'
        else:
            return f'{file_content_string}'
    except Exception as e:
        return f"Error: {e}"