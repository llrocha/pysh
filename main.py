from pysh_builtins import builtins
from pysh_launcher import launcher


PATH='/bin'
prompt = '> '
builtin_cmds = builtins()
cmd_launcher = launcher()


def debug_cmd(arguments):
    if(len(arguments)):
        print(f'COMMAND: {arguments[0]}')
        for i, arg in enumerate(arguments[1:]):
            print(f'ARGUMENT[{i}]: {arg}')

def execute_cmd(arguments):
    if(len(arguments)):
        if builtin_cmds.is_builtin(arguments):
            builtin_cmds.launch_builtin(arguments)
        else:
            cmd_launcher.launch_cmd(arguments)


if __name__ == '__main__':
    while(True):
        line = input(prompt)
        arguments = line.split()
        execute_cmd(arguments)
