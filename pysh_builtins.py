import os

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


class cd_builtin:
    def run(self, arguments):
        if len(arguments) == 2:
            os.chdir(arguments[1])
            return 0
        else:
            return 1


class echo_builtin:
    def run(self, arguments):
        print(' '.join(arguments[1:]))


class alias_builtin:
    def run(self, arguments):
        pass


class history_builtin:
    def run(self, arguments):
        pass


class exit_builtin:
    def run(self, arguments):
        if len(arguments) > 1:
            exit_value = int(arguments[1])
        else:
            exit_value = 0
        exit(exit_value)


class export_builtin:
    def run(self, arguments):
        pass


class unset_builtin:
    def run(self, arguments):
        pass


class source_builtin:
    def run(self, arguments):
        pass


class pwd_builtin:
    def run(self, arguments):
        pass


class type_builtin:
    def run(self, arguments):
        pass


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
            cd_builtin().run(arguments)
        elif command == 'echo':
            echo_builtin().run(arguments)
        elif command == 'alias':
            alias_builtin().run(arguments)
        elif command == 'history':
            history_builtin().run(arguments)
        elif command == 'export':
            export_builtin().run(arguments)
        elif command == 'unset':
            unset_builtin().run(arguments)
        elif command == 'source':
            source_builtin().run(arguments)
        elif command == 'exit':
            exit_builtin().run(arguments)
        elif command == 'pwd':
            pwd_builtin().run(arguments)
        elif command == 'type':
            type_builtin().run(arguments)
        else:
            raise NotImplementedError(command)

