"""
Shell interpreter written in Python
"""

from pysh_builtins import Builtins
from pysh_launcher import Launcher


PATH='/bin'
PROMPT = '> '
builtin_cmds = Builtins()
cmd_launcher = Launcher()



def execute_cmd(arguments):
    if len(arguments):
        if builtin_cmds.is_builtin(arguments=arguments):
            builtin_cmds.launch_builtin(arguments=arguments)
        else:
            cmd_launcher.launch_cmd(arguments=arguments)


if __name__ == '__main__':
    while True:
        line = input(PROMPT)
        arguments = line.split()
        execute_cmd(arguments=arguments)
