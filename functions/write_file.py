import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try :
        working_dir_abs = os.path.abspath(working_directory) #Returns complete dir path of working scope
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path)) #Fixes target dir
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs #Compares working/target dir
        if not valid_target_dir :
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir) :
            return (f'Error: Cannot write to "{file_path}" as it is a directory')
    except Exception as e :
        return (f'Error: {e}')
    
    os.makedirs(exist_ok = True)