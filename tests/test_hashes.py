import unittest
from cssdbpy import Connection

class Hashes(unittest.TestCase):

	def setUp(self):
		self.conn = Connection('127.0.0.1', 8888)

	def test_1hset(self):
		for i in xrange(0, 10):
			self.assertEqual(self.conn.execute('hset','test', 'test{}'.format(i), 1000), 1)

	def test_2hget(self):
		self.assertEqual(self.conn.execute('hget','test', 'test20'), 0)
		self.assertEqual(self.conn.execute('hget','test', 'test3'), 1000)

	def test_3hexists(self):
		self.assertEqual(self.conn.execute('hexists','test', 'test20'), 0)
		self.assertEqual(self.conn.execute('hexists','test', 'test3'), 1)

	def test_4hincr(self):
		self.assertEqual(self.conn.execute('hincr','test', 'test3', 1), 1001)
		self.assertEqual(self.conn.execute('hincr','test', 'test3', 100), 1101)

	def test_5hkeys(self):
		self.assertEqual(self.conn.execute('hkeys','test','','', -1), ['test{}'.format(i) for i in xrange(0, 10)])

	def test_5hsize(self):
		self.assertEqual(self.conn.execute('hsize','test'), 10)

	def test_5hgetall(self):
		self.assertEqual(self.conn.execute('hgetall','test'), ['test0', '1000', 'test1', '1000', 'test2', '1000', 'test3', '1101', 'test4', '1000', 
													'test5', '1000', 'test6', '1000', 'test7', '1000', 'test8', '1000', 'test9', '1000'])

	def test_7hscan(self):
		self.assertEqual(self.conn.execute('hscan','test','','',-1), ['test0', '1000', 'test1', '1000', 'test2', '1000', 'test3', '1101', 'test4', 
															'1000', 'test5', '1000', 'test6', '1000', 'test7', '1000', 'test8', '1000', 'test9', '1000'])

	def test_8hdel(self):
		self.assertEqual(self.conn.execute('hdel','test', 'empty_test'), 0)
		self.assertEqual(self.conn.execute('hdel','test', 'test3'), 1)

	def test_9hclear(self):
		self.assertEqual(self.conn.execute('hclear','test'), 9)
