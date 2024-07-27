#: pysh_launcher.py
"""Command launcher to run a shell commands"""

import subprocess

# pylint: disable=too-few-public-methods

class CommandLauncher():
    """command launcher"""
    def launch_cmd(self, arguments):
        """launch command"""
        if len(arguments):
            with subprocess.Popen(arguments) as process:
                # pid = process.pid
                process.wait()
            return process.returncode
        return 0
