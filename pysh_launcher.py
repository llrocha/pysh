#: pysh_launcher.py
import subprocess


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
