import os
import sys
import time

workers = []
for i in range(2):
    print('PARENT %d: Forking %s' % (os.getpid(), i))
    worker_pid = os.fork()
    if not worker_pid:
        print('WORKER %s: Starting' % i)
        time.sleep(2 + i)
        print('WORKER %s: Finishing' % i)
        sys.exit(i)
    workers.append(worker_pid)

for pid in workers:
    print('PARENT: Waiting for %s' % pid)
    done = os.waitpid(pid, 0)
    print('PARENT: Child done:', done)
