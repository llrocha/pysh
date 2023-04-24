import ast
import subprocess


class SnakeLauncher():
    def launch_cmd(self, arguments):
        if len(arguments):
            process = subprocess.Popen(arguments)
            pid = process.pid
            process.wait()

    def run_python(self, arguments):
        exec(' '.join(arguments))

    def is_valid_python_call(self, arguments):
        try:
            tree = ast.parse(arguments)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    return True
            return False
        except SyntaxError:
            return False
