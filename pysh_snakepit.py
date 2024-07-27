#: pysh_snakepit.py
import ast
import subprocess


class SnakeLauncher():
    """Launch python commands"""
    def launch_cmd(self, arguments):
        """launch command"""
        if len(arguments):
            process = subprocess.Popen(arguments)
            pid = process.pid
            process.wait()

    def run_python(self, arguments):
        """run a command line in python"""
        # pylint: disable-next=exec-used
        exec(' '.join(arguments))

    def is_valid_python_call(self, arguments):
        """check if is valid python call"""
        try:
            tree = ast.parse(arguments)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    return True
            return False
        except SyntaxError:
            return False
