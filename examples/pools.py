from cssdbpy.pool import PoolConnection
from multiprocessing import Lock, Pool
from time import time, sleep

# Very simple example pooling


poolconn = PoolConnection(32)

def send(name):
	print poolconn.execute("hset", "test", name, int(time()))
	sleep(0.001)

if __name__ == '__main__':
	pool = Pool(100)
	pool.map(send, [i for i in xrange(0, 100000)])
	pool.close()
	pool.join()