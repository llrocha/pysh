"""
    cd: change the current working directory
    echo: print a message to the terminal
    alias: create a shortcut for a longer command
    history: display a list of previously executed commands
    export: set an environment variable
    unset: remove an environment variable
    source: execute commands from a file in the current shell
    exit: exit the current shell
    pwd: print the current working directory
    type: determine whether a command is a shell built-in or an external executable
"""

class not_implemented_builtin:
    def run(self, arguments):
        print(f'builtin command [{arguments[0]}] is not implemented')


class exit_builtin:
    def run(self, arguments):
        if len(arguments) > 1:
            exit_value = int(arguments[1])
        else:
            exit_value = 0
        exit(exit_value)


class builtins:
    def __init__(self) -> None:
        self.builtins_cmds = [
            'cd', 'echo', 'alias', 'history', 'export',
            'unset', 'source', 'exit', 'pwd', 'type'
        ]

    def is_builtin(self, command):
        if(type(command) == list):
            return command[0].strip() in self.builtins_cmds
        else:
            return command.strip() in self.builtins_cmds
    
    def launch_builtin(self, arguments):
        command = arguments[0].strip()

        if command == 'cd':
            not_implemented_builtin().run(arguments)
        elif command == 'echo':
            not_implemented_builtin().run(arguments)
        elif command == 'alias':
            not_implemented_builtin().run(arguments)
        elif command == 'history':
            not_implemented_builtin().run(arguments)
        elif command == 'export':
            not_implemented_builtin().run(arguments)
        elif command == 'unset':
            not_implemented_builtin().run(arguments)
        elif command == 'source':
            not_implemented_builtin().run(arguments)
        elif command == 'exit':
            exit_builtin().run(arguments)
        elif command == 'pwd':
            not_implemented_builtin().run(arguments)
        elif command == 'type':
            not_implemented_builtin().run(arguments)
        else:
            raise NotImplementedError(command)

