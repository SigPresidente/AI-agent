import os

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try :
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir :
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(file_path) :
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        if not file_path.endswith('.py') :
            return (f'Error: "{file_path}" is not a Python file')
    except Exception as e :
        return (f'Error: {e}')
    
    command = ["python", absolute_file_path]
    command.extend(args)
    completed_process =subprocess.run(command, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=30, check=False, encoding=None, errors=None, text=True, env=None, universal_newlines=None)

    #Proseguire da passaggio 7#