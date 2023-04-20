import os

"""
    cd: change the current working directory, module CdBuiltin
    echo: print a message to the terminal, module EchoBuiltin
    alias: create a shortcut for a longer command, module AliasBuiltin
    history: display a list of previously executed commands, module HistoryBuiltin
    export: set an environment variable, module ExportBuiltin
    unset: remove an environment variable, module UnsetBuiltin
    source: execute commands from a file in the current shell, module SourceBuiltin
    exit: exit the current shell, module ExitBuiltin
    pwd: print the current working directory, module PwdBuiltin
    type: determine whether a command is a shell built-in or an external executable, module TypeBuiltin
"""

class NotImplementedBuiltin:
    def run(self, arguments):
        print(f'builtin command [{arguments[0]}] is not implemented')


class CdBuiltin:
    def run(self, arguments):
        if len(arguments) == 2:
            os.chdir(arguments[1])
            return 0
        else:
            return 1


class EchoBuiltin:
    def run(self, arguments):
        print(' '.join(arguments[1:]))


class AliasBuiltin:
    def run(self, arguments):
        pass


class HistoryBuiltin:
    def run(self, arguments):
        pass


class ExitBuiltin:
    def run(self, arguments):
        if len(arguments) > 1:
            exit_value = int(arguments[1])
        else:
            exit_value = 0
        exit(exit_value)


class ExportBuiltin:
    def run(self, arguments):
        pass


class UnsetBuiltin:
    def run(self, arguments):
        pass


class SourceBuiltin:
    def run(self, arguments):
        pass


class PwdBuiltin:
    def run(self, arguments):
        pass


class TypeBuiltin:
    def run(self, arguments):
        pass


class Builtins:
    def __init__(self) -> None:
        self.builtins_cmds = [
            'cd', 'echo', 'alias', 'history', 'export',
            'unset', 'source', 'exit', 'pwd', 'type'
        ]

    def is_builtin(self, command):
        if type(command) == list:
            return command[0].strip() in self.builtins_cmds
        else:
            return command.strip() in self.builtins_cmds

    def launch_builtin(self, arguments):
        command = arguments[0].strip()

        if command == 'cd':
            CdBuiltin().run(arguments)
        elif command == 'echo':
            EchoBuiltin().run(arguments)
        elif command == 'alias':
            AliasBuiltin().run(arguments)
        elif command == 'history':
            HistoryBuiltin().run(arguments)
        elif command == 'export':
            ExportBuiltin().run(arguments)
        elif command == 'unset':
            UnsetBuiltin().run(arguments)
        elif command == 'source':
            SourceBuiltin().run(arguments)
        elif command == 'exit':
            ExitBuiltin().run(arguments)
        elif command == 'pwd':
            PwdBuiltin().run(arguments)
        elif command == 'type':
            TypeBuiltin().run(arguments)
        else:
            raise NotImplementedError(command)

