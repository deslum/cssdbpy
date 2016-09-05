Welcome to cssdbpy's documentation!
===================================

What is SSDB?
-------------

SSDB is a high performace key-value(key-string, key-zset, key-hashmap) NoSQL database, an alternative to Redis.
SSDB is stable, production-ready and is widely used by many Internet companies including QIHU 360. It's repository is https://github.com/ideawu/ssdb


Features
--------

 * LevelDB client-server support, written in C/C++
 * Designed to store collection data
 * Persistent key-value, key-zset, key-map('hashmap') storage
 * Redis clients are supported
 * Client API supports including C++, PHP, Python, Cpy, Java, nodejs, Ruby, Go
 * Persistent queue service
 * Replication(master-slave), load balance
 * GUI administration tool(phpssdbadmin)
 * Built-in CLI nagios self-checks


About cssdbpy
-------------

cssdbpy is a simple SSDB client written on Cython. 5x faster standart ssdb client.
It's repository is https://github.com/deslum/cssdbpy


Install
-------

.. code-block:: bash

   pip install cssdbpy

or

.. code-block:: bash

   pip install https://github.com/deslum/cssdbpy

Connection
----------

.. code-block:: python

    >>> from cssdbpy import Connection
    >>> ssdb = Connection('127.0.0.1', 8888)

hset
---------------
Set the string value in argument as value of the key of a hashmap.

.. code-block:: python

    >>> ssdb.execute('hset', 'test', 'hash', '1')
    '1'

hget
----
Get the value related to the specified key of a hashmap

.. code-block:: python

    >>> ssdb.execute('hget', 'test', 'hash')
    '1'

hdel
----

Delete specified key of a hashmap.

.. code-block:: python

    >>> ssdb.execute('hdel', 'test', 'hash')
    '1'

hincr
-----

Increment the number stored at key in a hashmap by num. The num argument could be a negative integer. The old number is first converted to an integer before increment, assuming it was stored as literal integer.

.. code-block:: python

    >>> ssdb.execute('hincr', 'test', 'hash', 1)
    '1'

hscan
-----

List key-value pairs of a hashmap with keys in range (key_start, key_end]

.. code-block:: python

    >>> ssdb.execute('hscan', 'test', '', '', '-1')
    ['hash', '1']

hkeys
-----

List keys of a hashmap in range (key_start, key_end].

.. code-block:: python

    >>> ssdb.execute('hkeys', 'test', '', '', '-1')
    ['hash']

hsize
-----

Return the number of key-value pairs in the hashmap.

.. code-block:: python

    >>> ssdb.execute('hsize', 'test')
    3

hlist
-----

List hashmap names in range (name_start, name_end]

.. code-block:: python

    >>> ssdb.execute('hlist', '', '')
    3

hgetall
-------

Returns the whole hash, as an array of strings indexed by strings.

.. code-block:: python

    >>> ssdb.execute('hgetall', 'test')
    3

hclear
------

Delete all keys in a hashmap.

.. code-block:: python

    >>> ssdb.execute('hgetall', 'test')
    3

multi_hset
----------

Set multiple key-value pairs(kvs) of a hashmap in one method call.

.. code-block:: python

    >>> ssdb.execute('hgetall', 'test')
    3

multi_hget
----------

Get the values related to the specified multiple keys of a hashmap.

.. code-block:: python

    >>> ssdb.execute('hgetall', 'test')
    3

multi_hdel
----------

Delete specified multiple keys in a hashmap.

.. code-block:: python

    >>> ssdb.execute('hgetall', 'test')
    3


Questions?
---------------------------

randomazer@gmail.com
