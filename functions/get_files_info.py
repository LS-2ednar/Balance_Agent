import os

def get_files_info(working_directory, directory=None):

    cwd = os.path.abspath(working_directory)
    wd = cwd
    
    if directory:
        wd = os.path.abspath(os.path.join(working_directory,directory))

    if not wd.startswith(cwd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(wd):
        return f'Error: "{directory}" is not a directory'
    
    try:
        return_string = []
        for file in os.listdir(os.path.join(cwd,directory)):
            file_path=os.path.join(wd,file)
            return_string.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")

        return "\n".join(return_string)
    except Exception as e:
        return f"Error listing files: {e}"
