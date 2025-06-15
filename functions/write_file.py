import os 

def write_file(working_directory, file_path, content):

    cwd = os.path.abspath(working_directory)
    wd = os.path.abspath(os.path.join(working_directory,file_path))

    if not wd.startswith(cwd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(wd):
            os.makedirs(wd)
            with open(wd, "w") as f:
                    f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        else:
            with open(wd, "w") as f:
                    f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"