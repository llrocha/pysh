"""
Shell interpreter written in Python
"""
import ast

from pysh_builtins import BuiltinLauncher
from pysh_launcher import CommandLauncher


PATH = '/bin'
PROMPT = '$ '
COMMAND = ''
builtin_launcher = BuiltinLauncher()
cmd_launcher = CommandLauncher()


def run_python(arguments):
    exec(' '.join(arguments))


def is_valid_python_call(arguments):
    try:
        tree = ast.parse(arguments)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                return True
        return False
    except SyntaxError:
        return False


def execute_cmd(arguments):
    if len(arguments):
        if builtin_launcher.is_builtin(arguments):
            builtin_launcher.launch_builtin(arguments)
        elif is_valid_python_call(' '.join(arguments)):
            run_python(arguments)
        else:
            cmd_launcher.launch_cmd(arguments)


if __name__ == '__main__':
    while True:
        try:
            line = input(PROMPT)
            if line[-1:] != '\\':
                COMMAND += line
                execute_cmd(COMMAND.split())
                COMMAND = ''
            else:
                COMMAND += line[:-1]
        except NotImplementedError as e:
            print(f'{e} is not implemented yet')
        except KeyboardInterrupt as e:
            print(e)
        except Exception as e:
            print(e)
