from multiprocessing import Lock
from credis import Connection

cdef class PoolConnection(object):

    cdef list __buffer
    cdef int __lenght
    cdef object __lock

    def __cinit__(self, lenght, host = "127.0.0.1", port = 8888, password = None):
        self.__buffer = list()
        self.__lenght = 0
        self.__lock = Lock()
        for x in xrange(0, lenght):
            connection = Connection(host, port, password)
            self.__buffer.append(connection)
            self.__lenght = len(self.__buffer)

    def _get_connection(self):
        self.__lock.acquire()
        connection = self.__buffer.pop()
        self.__lenght = len(self.__buffer)
        self.__lock.release()
        return connection

    def _return_connection(self, connection):
        self.__lock.acquire()
        self.__buffer.append(connection)
        self.__lenght = len(self.__buffer)
        self.__lock.release() 

    def execute(self, *args):
        conn = self._get_connection()
        result = conn.execute(*args)
        self._return_connection(conn)
        return result

    def __cdel__(self):
        for x in xrange(0, self.lenght):
            connection = self.__buffer.pop(0)
            connection.close()
        self.__lenght = 0