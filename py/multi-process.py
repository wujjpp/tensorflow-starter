from multiprocessing import Process
import multiprocessing
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    print('My parent process is /bin/bash and it\'s id is: %s' % os.getppid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    print('CPU count: %s' % (multiprocessing.cpu_count(), ))
