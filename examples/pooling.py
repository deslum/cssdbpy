from cssdbpy import Connection

'''

This is simple example pooling Connection on Python

TODO

* Rewrite in Cython
* Add semaphore
* Add multithreading
* Refactoring code

'''

class PoolConnection:

	__instance = None
	__buffer = list()
	__lenght = 0

	def __init__(self, lenght, host = "127.0.0.1", port = 8888, password = None):
		
		if PoolConnection.__instance != None:
			raise NotImplemented("This is a singleton class.")

		for x in xrange(0, lenght):
			connection = Connection(host, port, password)
			self.__buffer.append(connection)
			self.__lenght +=1

	@staticmethod
	def create(lenght):
		if PoolConnection.__instance == None:
			PoolConnection.__instance = PoolConnection(lenght)
		return PoolConnection.__instance

	def get_connection(self):
		if len(self.__buffer) > 0:
			self.__lenght =-1
			connection = self.__buffer.pop(0)
			return connection


	def return_connection(self, connection):
		self.__buffer.append(connection)


	def execute(self, *args):
		__retry_count = 0
		while __retry_count<5:
			conn = pool.get_connection()
			if conn:
				result = conn.execute(*args)
				self.return_connection(conn)
				return result
			else:
				__retry_count+=1


if __name__ == '__main__':
	pool = PoolConnection.create(4)
	for i in xrange(0, 15000):
		print(pool.execute("hexists", "test", "one"))