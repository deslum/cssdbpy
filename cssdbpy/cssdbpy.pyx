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


    def __cinit__(self, host = b'127.0.0.1', port = 8888, password = None):
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
        cdef list send_object = []
        for arg in args:
            send_object.append(SEND_TEMPLATE.format(len(str(arg)), arg))
        send_object.append(END_SEND)
        self.sock.send(''.join(send_object))
        return self._read()

    def pipeline(self, *args):
        cdef list response_object = []
        for subargs in args:
            response_object.append(self.execute(*subargs))
        return response_object


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
        elif status == NOT_FOUND:
            return list(b'0')
        return args

    def __del__(self):
        self.sock.close()
