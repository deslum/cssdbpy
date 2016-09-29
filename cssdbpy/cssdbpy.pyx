import socket

DEF SEND_TEMPLATE = b'{}\n{}\n'
DEF END_SEND = b'\n'
DEF READ_BUFFER = 1024*8
DEF OK = b'ok'
DEF NOT_FOUND = b'not_found'
DEF END_RESPONSE = b'\n\n'


cdef class Connection(object):

    cdef object sock
    cdef bytes host
    cdef int port
    cdef bytes password


    def __init__(self, host = b'127.0.0.1', port = 8888, password = None):
        self.host = host
        self.port = port
        self.password = password
        self.sock = None
        self._connect()

    cpdef _connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.sock.connect((self.host, self.port))
        if self.password:
            self.execute('auth', self.password)
	
    def execute(self, *args):
        map(lambda field: self.sock.send(SEND_TEMPLATE.format(len(str(field)), field)), args)
        self.sock.send(END_SEND)
        return self._read()

    cdef _read(self, bytes data = b''):
        cdef bytes tmp = b''
        while tmp != END_RESPONSE:
            resp = self.sock.recv(READ_BUFFER)
            data += resp
            tmp = resp[-2:]
        cdef list ndata = self._parse(data)
        if ndata and len(ndata)<2:
            return int(ndata.pop())
        return ndata

    cdef list _parse(self, char* data):
        cdef list ndata = data.split(b'\n')
        status, args = ndata.pop(1), ndata[2::2]
        if status == OK:
            return filter(lambda x: x, args)
        if status == NOT_FOUND:
            return list(b'0')
        return list(data)

    def __del__(self):
        self.sock.close()