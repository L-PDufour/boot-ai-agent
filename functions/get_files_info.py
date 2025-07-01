import os


def get_files_info(working_directory, directory):
    if directory == ".":
        directory = ""

    join_path = os.path.join(working_directory, directory)

    # Security check: ensure the resolved path is within working_directory
    abs_working_dir = os.path.abspath(working_directory)
    abs_join_path = os.path.abspath(join_path)

    if not abs_join_path.startswith(abs_working_dir):
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isdir(join_path):
        print(f'Error: "{directory}" is not a directory')
        return

    dir_content = os.listdir(join_path)
    string = []
    for item in dir_content:
        full_path = os.path.join(join_path, item)
        size = os.path.getsize(full_path)
        isfile = os.path.isfile(full_path)
        string.append(f"- {item}: file_size={size} bytes, is_dir={not isfile}")

    return string
