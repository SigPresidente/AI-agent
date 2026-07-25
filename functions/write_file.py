import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try :
        working_dir_abs = os.path.abspath(working_directory) #Returns complete dir path of working scope
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path)) #Fixes target dir
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs #Compares working/target dir
        if not valid_target_dir :
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_dir) :
            return (f'Error: Cannot write to "{file_path}" as it is a directory')
        os.makedirs(os.path.dirname(target_dir), exist_ok = True)
        with open(target_dir, "w") as f:
            f.write(content)
            return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except Exception as e :
        return (f'Error: {e}')
    
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites content to a specific file, in a specified directory",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
            "required": ["file_path", "content"]
        },
    },
}      