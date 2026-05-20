import os
from config import CHAR_LIMIT

def get_file_content(working_directory: str, file_path: str) -> str :
    try :
        working_dir_abs = os.path.abspath(working_directory) #Returns complete dir path of working scope
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path)) #Fixes target dir
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs #Compares working/target dir
        if not valid_target_dir :
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isdir(file_path) :
            return (f'Error: File not found or is not a regular file: "{file_path}"')
    except Exception as e :
        return (f'Error: {e}')

    with open(file_path, "r") as f:
        file_content_string = f.read(CHAR_LIMIT)
        if f.read(1):
            file_content_string += f'[...File "{file_path}" truncated at {CHAR_LIMIT} characters]'
        print(f"File content: {file_content_string}")