Simple SSDB client written on CPython.

Tutorial
========

hset/hget
---------------

.. code-block:: python

    >>> from ssdbpy import ssdbpy
    >>> ssdb = Connection('127.0.0.1', 8888)
    >>> ssdb.execute('hset', 'test', 'hash', '1')
    '1'
    >>> conn.execute('hget', 'test', 'hash')
    '1'

hscan/hkeys
----------------

.. code-block:: python

    >>> ssdb.execute('hscan', 'test', '', '', '-1')
    ['hash', '1']
    >>> conn.execute('hkeys', 'test', '', '', '-1')
    ['hash']