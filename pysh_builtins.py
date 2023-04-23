import os

from abc import ABC, abstractmethod

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

class BuiltinStrategy(ABC):
    @abstractmethod
    def run(self, arguments):
        pass


class CdBuiltin(BuiltinStrategy):
    def run(self, arguments):
        if len(arguments) == 2:
            os.chdir(arguments[1])
            return 0
        else:
            return 1


class EchoBuiltin(BuiltinStrategy):
    def run(self, arguments):
        print(' '.join(arguments[1:]))


class AliasBuiltin(BuiltinStrategy):
    def run(self, arguments):
        raise NotImplementedError('alias')


class HistoryBuiltin(BuiltinStrategy):
    def run(self, arguments):
        raise NotImplementedError('history')


class ExitBuiltin:
    def run(self, arguments):
        if len(arguments) > 1:
            exit_value = int(arguments[1])
        else:
            exit_value = 0
        exit(exit_value)


class ExportBuiltin(BuiltinStrategy):
    def run(self, arguments):
        raise NotImplementedError('export')


class UnsetBuiltin(BuiltinStrategy):
    def run(self, arguments):
        raise NotImplementedError('unset')


class SourceBuiltin(BuiltinStrategy):
    def run(self, arguments):
        raise NotImplementedError('source')


class PwdBuiltin(BuiltinStrategy):
    def run(self, arguments):
        raise NotImplementedError('pwd')


class TypeBuiltin(BuiltinStrategy):
    def run(self, arguments):
        raise NotImplementedError('type')


class BuiltinLauncher:
    def __init__(self) -> None:
        self.builtins_cmds = {
            'cd': CdBuiltin(),
            'echo': EchoBuiltin(),
            'alias': AliasBuiltin(),
            'history': HistoryBuiltin(),
            'export': ExportBuiltin(),
            'unset': UnsetBuiltin(),
            'source': SourceBuiltin(),
            'exit': ExitBuiltin(),
            'pwd': PwdBuiltin(),
            'type': TypeBuiltin(),
        }

    def is_builtin(self, command):
        internal_command = command
        if type(command) == list:
            internal_command = command[0]
        return internal_command.strip() in self.builtins_cmds

    def launch_builtin(self, arguments):
        command_name = arguments[0].strip()
        if command_name in self.builtins_cmds:
            builtin_strategy = self.builtins_cmds[command_name]
            builtin_strategy.run(arguments)
        else:
            raise NotImplementedError(command_name)

