import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False

        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        target_items = os.listdir(target_dir)
        lines = []
        for name in target_items:
            item_path = os.path.join(target_dir, name)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            line = f"- {name}: file_size={size} bytes, is_dir={is_dir}"
            lines.append(line)
        result = "\n".join(lines)
        return result
    except Exception as e:
        return f"Error: {e}"
