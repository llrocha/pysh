import subprocess


class CommandLauncher():
    def launch_cmd(self, arguments):
        if len(arguments):
            process = subprocess.Popen(arguments)
            pid = process.pid
            process.wait()
            return process.returncode
        else:
            return 0
