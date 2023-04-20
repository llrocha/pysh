import os

from pysh_builtins import builtins

PATH='/bin'
prompt = '> '
builtin_cmds = builtins()


def debug_cmd(arguments):
    if(len(arguments)):
        print(f'COMMAND: {arguments[0]}')
        for i, arg in enumerate(arguments[1:]):
            print(f'ARGUMENT[{i}]: {arg}')

def launch_cmd(arguments):
    if(len(arguments)):
        pid = os.fork()
        if pid == 0:
            print('\nchild process, pid:', os.getpid())
            #print(f'{arguments}!')
            os.system(' '.join(arguments))
        elif pid > 0:
            print('parent process, pid:', os.getpid())
            os.waitpid(pid, os.WNOHANG)
            print('child process finalized, pid:', pid)
        else:
            print(f'error creating child process {arguments}!')

def is_builtin(arguments):
    return arguments[0].strip() in builtin_cmds

def launch_builtin(arguments):
    command = arguments[0].strip()
    if command == 'exit':
        if len(arguments) > 1:
            exit_value = int(arguments[1])
        else:
            exit_value = 0
        exit(exit_value)

def execute_cmd(arguments):
    if(len(arguments)):
        if builtin_cmds.is_builtin(arguments):
            builtin_cmds.launch_builtin(arguments)
        else:
            launch_cmd(arguments)

while(True):
    line = input(prompt)
    arguments = line.split()    
    execute_cmd(arguments)
