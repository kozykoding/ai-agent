import os, subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False

        valid_target_path = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]

        if args is not None:
            command.extend(args)
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        out_text = result.stdout.strip()
        err_text = result.stderr.strip()
        output = []

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if out_text:
            output.append(f"STDOUT:{out_text}")
        if err_text:
            output.append(f"STDERR:{err_text}")
        if not out_text and not err_text and result.returncode == 0:
            output.append("No output produced")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Required file path to execute Python files with optional arguments",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Array of optional args to execute Python files with optional arguments",
            ),
        },
    ),
)
