"""
Shell interpreter written in Python
"""

from pysh_builtins import BuiltinLauncher
from pysh_launcher import CommandLauncher


PATH='/bin'
PROMPT = '> '
builtin_launcher = BuiltinLauncher()
cmd_launcher = CommandLauncher()



def execute_cmd(arguments):
    if len(arguments):
        if builtin_launcher.is_builtin(arguments):
            builtin_launcher.launch_builtin(arguments)
        else:
            cmd_launcher.launch_cmd(arguments)


if __name__ == '__main__':
    while True:
        try:
            line = input(PROMPT)
            execute_cmd(line.split())
        except NotImplementedError as e:
            print(f'{e} is not implemented yet')
        except Exception as e:
            print(e)
