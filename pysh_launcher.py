import os


class CommandLauncher():
    def launch_cmd(self, arguments):
        if len(arguments):
            pid = os.fork()
            if pid == 0:
                print('\nchild process, pid:', os.getpid())
                #print(f'{arguments}!')
                os.system(' '.join(arguments))
            elif pid > 0:
                print('parent process, pid:', os.getpid())
                os.waitpid(pid, os.WNOHANG)
                print('child process finalized, pid:', pid)
            else:
                print(f'error creating child process {arguments}!')
