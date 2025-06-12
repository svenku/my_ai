import os

def get_files_info(working_directory, directory=None):
    """
    Get information about files in a directory.

    Args:
    working_directory (str): The base directory to search in.
    directory (str, optional): The specific subdirectory to search in. Defaults to None.

    Returns:
    list: A list of dictionaries containing file information. Alternatively, a string with error messages.
    """
          
    if directory is not None:
        abs_working_directory = os.path.abspath(working_directory)
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))
        if not abs_directory.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_directory):
            return f'Error: "{directory}" is not a directory'
    else:
        directory = ""
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    entries = os.listdir(abs_directory)
    result_lines = []
    for entry in entries:
        entry_path = os.path.join(abs_directory, entry)
        is_dir = os.path.isdir(entry_path)
        size = os.path.getsize(entry_path)
        result_lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(result_lines)

