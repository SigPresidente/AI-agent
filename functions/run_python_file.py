import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try :
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir :
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_dir) :
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        if not file_path.endswith('.py') :
            return (f'Error: "{file_path}" is not a Python file')
    except Exception as e :  # noqa: BLE001
        return (f'Error: {e}')
    
    try :
        command = ["python", target_dir]
        if (args is not None) :
            command.extend(args)
        completed_process = subprocess.run(command, stdin=None, input=None, capture_output=True, shell=False, cwd=working_directory, timeout=30, 
                                       check=False, encoding=None, errors=None, text=True, env=None)
        if completed_process.returncode != 0 :
            return (f'Process exited with code {completed_process.returncode}') 
        elif (completed_process.stdout is None and completed_process.stderr is None) :
            return ('No output produced')
        else :
            return (f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}')
    except Exception as e :  # noqa: BLE001
        return (f'Error: executing Python file: {e}')

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes the specified Python file in the specified directory, with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional list of arguments to pass to the Python file",
                },
            },
            "required" : ["file_path"]
        },
    },
}  