import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)
    abs_join_path = os.path.abspath(file_path)

    # if not abs_join_path.startswith(abs_working_dir):
    #     print(
    #         f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    #     )
    #     return

    # if not os.path.isfile(abs_join_path):
    #     print(f'Error: File not found or is not a regular file: "{file_path}"')
    #     return

    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    return file_content_string
