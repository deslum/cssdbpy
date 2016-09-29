from cssdbpy import Connection
import pyssdb 
from credis import Connection as RedisConnection
from SSDB import SSDB
from ssdb import SSDB as ssdbpy
from time import time

HOST = '127.0.0.1'
PORT = 8888
FIELDS = 80000.0

# #Oficial client SSDB
def SSDB_test():
	conn = SSDB(HOST, PORT)
	start_time = time()
	map(lambda x: conn.request('hset',['cssdbpy',str(i), 1]), [i for i in xrange(10000,90000)])
	print 'hset', FIELDS/(time()-start_time)
	start_time = time()
	conn.request('hscan',['cssdbpy','','', -1])
	print 'hscan', FIELDS/(time()-start_time)
	for action in ['hget', 'hdel']:
		start_time = time()
		map(lambda x: conn.request(action,['cssdbpy',str(i)]), [i for i in xrange(10000,90000)])
		print action, FIELDS/(time()-start_time)

# #https://github.com/ifduyue/pyssdb
def pyssdb_test():
	conn = pyssdb.Client(HOST, PORT)
	start_time = time()
	map(lambda x: conn.hset('cssdbpy',str(i), 1), [i for i in xrange(10000,90000)])
	print 'hset', FIELDS/(time()-start_time)
	start_time = time()
	conn.hscan('cssdbpy','','', -1)
	print 'hscan', FIELDS/(time()-start_time)
	start_time = time()
	map(lambda x: conn.hget('cssdbpy',str(i)), [i for i in xrange(10000,90000)])
	print 'hget', FIELDS/(time()-start_time)
	start_time = time()
	map(lambda x: conn.hdel('cssdbpy',str(i)), [i for i in xrange(10000,90000)])
	print 'hdel', FIELDS/(time()-start_time)

# #https://github.com/wrongwaycn/ssdb-py
def ssdbpy_test():
	conn = ssdbpy(HOST, PORT)
	start_time = time()
	map(lambda x: conn.hset('cssdbpy',str(i), 1), [i for i in xrange(10000,90000)])
	print 'hset', FIELDS/(time()-start_time)
	start_time = time()
	conn.hscan('cssdbpy','','', 10000000)
	print 'hscan', FIELDS/(time()-start_time)
	start_time = time()
	map(lambda x: conn.hget('cssdbpy',str(i)), [i for i in xrange(10000,90000)])
	print 'hget', FIELDS/(time()-start_time)
	start_time = time()
	map(lambda x: conn.hdel('cssdbpy',str(i)), [i for i in xrange(10000,90000)])
	print 'hdel', FIELDS/(time()-start_time)


#https://github.com/deslum/cssdbpy
def cssdbpy_test():
	conn = Connection(HOST, PORT)
	start_time = time()
	map(lambda x: conn.execute('hset','cssdbpy',str(i), 1), [i for i in xrange(10000,90000)])
	print 'hset', FIELDS/(time()-start_time)
	start_time = time()
	conn.execute('hscan','cssdbpy','','', -1)
	print FIELDS, (time()-start_time)
	print 'hscan', FIELDS/(time()-start_time)
	for action in ['hget', 'hdel']:
		start_time = time()
		map(lambda x: conn.execute(action,'cssdbpy',str(i)), [i for i in xrange(10000,90000)])
		print action, FIELDS/(time()-start_time)



if __name__ == '__main__':
	SSDB_test()
	pyssdb_test()
	ssdbpy_test()
	cssdbpy_test()
