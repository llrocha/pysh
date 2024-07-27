#: pysh_launcher.py
"""Command launcher to run a shell commands"""

import subprocess

# pylint: disable=too-few-public-methods

class CommandLauncher():
    """command launcher"""
    def launch_cmd(self, arguments):
        """launch command"""
        if len(arguments):
            process = subprocess.Popen(arguments)
            pid = process.pid
            process.wait()
            return process.returncode
        else:
            return 0
