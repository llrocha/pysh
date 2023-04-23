import subprocess


class CommandLauncher():
    def launch_cmd(self, arguments):
        if len(arguments):
            process = subprocess.Popen(arguments)
            pid = process.pid
            print(f'child process, pid: {pid}')
            process.wait()
            print(f'child process finalized, pid: {pid}')