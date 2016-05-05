Simple SSDB client written on Cython.

**Testing. Not production ready.**

Tutorial
========

hset/hget
---------------

.. code-block:: python

    >>> from ssdbpy import SSDBPy
    >>> ssdb = SSDBPy('127.0.0.1', 8888)
    >>> ssdb.execute('hset', 'test', 'hash', '1')
    '1'
    >>> ssdb.execute('hget', 'test', 'hash')
    '1'

hscan/hkeys
----------------

.. code-block:: python

    >>> ssdb.execute('hscan', 'test', '', '', '-1')
    ['hash', '1']
    >>> ssdb.execute('hkeys', 'test', '', '', '-1')
    ['hash']
