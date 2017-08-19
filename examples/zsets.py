from cssdbpy import Connection
import md5

if __name__ == '__main__':
	conn = Connection('127.0.0.1', 8888)
	for i in xrange(0, 10000):
		md5word = md5.new('word{}'.format(i)).hexdigest()
		create = conn.execute('zset','ztest', md5word, i)
		value = conn.execute('zget','ztest', md5word)
		conn.execute('zincr','ztest', md5word)
		conn.execute('zincr','ztest', md5word, 10)
		exists = conn.execute('zexists','ztest', md5word)
		delete = conn.execute('zdel','ztest', md5word)
		print md5word, value, create, exists, delete
	print conn.execute('zscan', 'ztest', '', 0, 1000, 10)
	print conn.execute('zrscan', 'ztest', 1000, 0, 10)
	conn.execute('zclean','words')