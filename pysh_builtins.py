#: pysh_builtins.py
"""This class is built to run built-in command shell"""

import os
import sys

from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods

class BuiltinStrategy(ABC):
    """Abstract base class for built in commands"""
    @abstractmethod
    def run(self, arguments):
        """abstract run method"""


class CdBuiltin(BuiltinStrategy):
    """CdBuiltin: change the current working directory"""
    def run(self, arguments):
        if len(arguments) == 2:
            os.chdir(arguments[1])
            return 0
        return 1


class EchoBuiltin(BuiltinStrategy):
    """EchoBuiltin: print a message to the terminal"""
    def run(self, arguments):
        print(' '.join(arguments[1:]))


class AliasBuiltin(BuiltinStrategy):
    """AliasBuiltin: create a shortcut for a longer command"""
    def run(self, arguments):
        raise NotImplementedError('alias')


class HistoryBuiltin(BuiltinStrategy):
    """HistoryBuiltin: display a list of previously executed commands"""
    def run(self, arguments):
        raise NotImplementedError('history')


class ExitBuiltin:
    """ExitBuiltin: exit the current shell"""
    def run(self, arguments):
        if len(arguments) > 1:
            exit_value = int(arguments[1])
        else:
            exit_value = 0
        sys.exit(exit_value)


class ExportBuiltin(BuiltinStrategy):
    """ExportBuiltin: set an environment variable"""
    def run(self, arguments):
        raise NotImplementedError('export')


class UnsetBuiltin(BuiltinStrategy):
    """UnsetBuiltin: remove an environment variable"""
    def run(self, arguments):
        raise NotImplementedError('unset')


class SourceBuiltin(BuiltinStrategy):
    """SourceBuiltin: execute commands from a file in the current shell"""
    def run(self, arguments):
        raise NotImplementedError('source')


class PwdBuiltin(BuiltinStrategy):
    """PwdBuiltin: print the current working directory"""
    def run(self, arguments):
        print(os.getcwd())


class TypeBuiltin(BuiltinStrategy):
    """determine whether a command is a shell built-in or an external executable"""
    def run(self, arguments):
        raise NotImplementedError('type')


class BuiltinLauncher:
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
        type: determine whether a command is a shell built-in or an external executable
        module TypeBuiltin
    """
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
        """check builtin command"""
        internal_command = command
        if isinstance(command, list):
            internal_command = command[0]
        return internal_command.strip() in self.builtins_cmds

    def launch_builtin(self, arguments):
        """launch builtin command"""
        command_name = arguments[0].strip()
        if command_name in self.builtins_cmds:
            builtin_strategy = self.builtins_cmds[command_name]
            builtin_strategy.run(arguments)
        else:
            raise NotImplementedError(command_name)
