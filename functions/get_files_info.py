import os

def get_files_info(working_directory, directory=None):
    if directory != working_directory:
        return f'Error: Cannot list"{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(directory):
        return f'Error: "{direcotry}"is not a directory'
    else:
        return_string = ""
        for file in os.listdir(directory):
            return_string += file+": file_size="+os.path.getsize(os.path.join(directory,file)) +" bytes, is_dir="+os.path.isdir(file)
        print(return_string)
        return return_string

