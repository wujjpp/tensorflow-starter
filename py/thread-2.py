import threading

# 假定这是你的银行存款:
balance = 0
locker = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 获取线程锁
        locker.acquire()

        try:
            change_it(n)
        finally:
            # 释放锁
            locker.release()


t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

