"""
Shell interpreter written in Python
"""

from pysh_builtins import builtins
from pysh_launcher import launcher


PATH='/bin'
PROMPT = '> '
builtin_cmds = builtins()
cmd_launcher = launcher()



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
