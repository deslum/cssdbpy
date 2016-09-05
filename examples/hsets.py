from cssdbpy import Connection
from time import time
import md5

if __name__ == '__main__':
	conn = Connection('127.0.0.1', 8888)
	for i in xrange(0, 1000):
		md5word = md5.new('word{}'.format(i)).hexdigest()
		create = conn.execute('hset','words', md5word, int(time()))
		value = conn.execute('hget','words', md5word)
		exists = conn.execute('hexists','words', md5word)
		delete = conn.execute('hdel','words', md5word)
		print md5word, value, create, exists, delete
	print conn.execute('hscan', 'words', '', '', 100)
	conn.execute('hclear','words')
