from cssdbpy import Connection
from SSDB import SSDB
from time import time

def cssdbpy_test():
	conn = Connection('192.168.0.103', 8888)
	start_time = time()
	map(lambda x: conn.execute('hset','cssdbpy',str(i), 1), [i for i in xrange(10000,90000)])
	print 'hset', time()-start_time
	start_time = time()
	conn.execute('hscan','cssdbpy','','', -1)
	print 'hscan', time()-start_time
	for action in ['hget', 'hdel']:
		start_time = time()
		map(lambda x: conn.execute(action,'cssdbpy',str(i)), [i for i in xrange(10000,90000)])
		print action, time()-start_time

def SSDB_test():
	conn = SSDB('192.168.0.103', 8888)
	start_time = time()
	map(lambda x: conn.request('hset',['cssdbpy',str(i), 1]), [i for i in xrange(10000,90000)])
	print 'hset', time()-start_time
	start_time = time()
	conn.request('hscan',['cssdbpy','','', -1])
	print 'hscan', time()-start_time
	for action in ['hget', 'hdel']:
		start_time = time()
		map(lambda x: conn.request(action,['cssdbpy',str(i)]), [i for i in xrange(10000,90000)])
		print action, time()-start_time	


if __name__ == '__main__':
	SSDB_test()
	cssdbpy_test()