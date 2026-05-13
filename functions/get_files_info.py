def get_files_info(working_directory, directory="."):
    os.path.abspath() #Gets the absolute path of the current working directory

    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))