import threading


def hap(num):
    ret = 0
    for i in range(1, num + 1):
        ret += i
    print('1+2+3+.....+', num, '=', ret)


th1 = threading.Thread(target=hap, args=(1000, ))
th2 = threading.Thread(target=hap, args=(100000, ))
th3 = threading.Thread(target=hap, args=(10000000, ))

th1.start()
th2.start()
th3.start()
