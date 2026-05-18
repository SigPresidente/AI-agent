import os

def get_files_info(working_directory, directory="."):
    try :
        working_dir_abs = os.path.abspath(working_directory) #Returns complete dir path of working scope
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory)) #Fixes target dir
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs #Compares working/target dir
        if not valid_target_dir :
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir) :
            return (f'Error: "{directory}" is not a directory')
        print(f'Success: "{directory}" is within the working directory')
    except Exception as e :
        return (f'Error: {e}')
    
    for item in os.listdir(target_dir) :
        try :
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item)
            file_name = os.path.isfile(item_path)
            file_is_dir = os.path.isdir(item_path)
            print(f"{file_name}: {file_size} bytes, is_dir={file_is_dir}")
        except Exception as e :
            return (f"Error: {e}")
         