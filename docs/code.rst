======
Client
======

.. automodule:: ssdb.client

   .. autoclass:: SSDB

   .. autoclass:: StrictSSDB


   Key/Value 
   ^^^^^^^^^

   A container of (key, value) pairs in ssdb. A key name maps a string value.

   .. code-block:: python

      >>> from ssdb.client import SSDB
      >>> ssdb = SSDB()
      >>> ssdb.multi_set(set_a='a', set_b='b', set_c='c', set_d='d')
      >>> ssdb.multi_set(set_x1='x1', set_x2='x2', set_x3='x3', set_x4='x4')
      >>> ssdb.multi_set(set_abc='abc', set_count=10)

   get
   """
   .. automethod:: StrictSSDB.get

   getset
   """"""
   .. automethod:: StrictSSDB.getset

   set
   """
   .. automethod:: StrictSSDB.set

   add
   """
   The same is `set`_.

   setnx
   """""
   .. automethod:: StrictSSDB.setnx

   expire
   """"""
   .. automethod:: StrictSSDB.expire

   ttl
   """
   .. automethod:: StrictSSDB.ttl

   setx
   """"
   .. automethod:: SSDB.setx

   delete
   """"""
   .. automethod:: StrictSSDB.delete

   remove
   """"""
   The same is `delete`_.

   exists
   """"""
   .. automethod:: StrictSSDB.exists

   incr
   """"
   .. automethod:: StrictSSDB.incr

   decr
   """"
   .. automethod:: StrictSSDB.decr

   getbit
   """"""
   .. automethod:: StrictSSDB.getbit

   setbit
   """"""
   .. automethod:: StrictSSDB.setbit

   countbit
   """"""""
   .. automethod:: StrictSSDB.countbit

   substr
   """"""
   .. automethod:: StrictSSDB.substr

   strlen
   """"""
   .. automethod:: StrictSSDB.strlen

   multi_set
   """""""""
   .. automethod:: StrictSSDB.multi_set

   mset
   """"
   The same is `multi_set`_.

   multi_get
   """""""""
   .. automethod:: StrictSSDB.multi_get

   mget
   """"
   The same is `multi_get`_.

   multi_del
   """""""""
   .. automethod:: StrictSSDB.multi_del

   mdel
   """"
   The same is `multi_del`_.

   keys
   """"
   .. automethod:: StrictSSDB.keys

   scan
   """"
   .. automethod:: StrictSSDB.scan

   rscan
   """""
   .. automethod:: StrictSSDB.rscan

   Hash
   ^^^^

   A container of (key, dict) pairs in ssdb. A hash name maps a dict which
   contains key/value pairs

   .. code-block:: python

      >>> from ssdb.client import SSDB
      >>> ssdb = SSDB()
      >>> ssdb.multi_hset('hash_1', a='A', b='B', c='C', d='D', e='E', f='F',
      ...                 g='G')
      >>> ssdb.multi_hset('hash_2',
      ...                 key1=42,
      ...                 key2=3.1415926,
      ...                 key3=-1.41421,
      ...                 key4=256,
      ...                 key5='e',
      ...                 key6='log'
      ...                )

   hget
   """"
   .. automethod:: StrictSSDB.hget

   hset
   """"
   .. automethod:: StrictSSDB.hset

   hadd
   """"
   The same is `hadd`_.

   hclear
   """"""
   .. automethod:: StrictSSDB.hclear

   hdel
   """"
   .. automethod:: StrictSSDB.hdel

   hremove
   """""""
   The same is `hdel`_.

   hash_exists
   """""""""""
   .. automethod:: StrictSSDB.hash_exists

   hexists
   """""""
   .. automethod:: StrictSSDB.hexists

   hincr
   """""
   .. automethod:: StrictSSDB.hincr

   hdecr
   """""
   .. automethod:: StrictSSDB.hdecr

   hsize
   """""
   .. automethod:: StrictSSDB.hsize

   hlen
   """"
   The same is `hsize`_.

   multi_hget
   """"""""""
   .. automethod:: StrictSSDB.multi_hget

   hmget
   """""
   The same is `multi_hget`_.

   multi_hset
   """"""""""
   .. automethod:: StrictSSDB.multi_hset

   hmset
   """""
   The same is `multi_hset`_.

   multi_hdel
   """"""""""
   .. automethod:: StrictSSDB.multi_hdel

   hmdel
   """""
   The same is `multi_hdel`_.

   hlist
   """""
   .. automethod:: StrictSSDB.hlist

   hrlist
   """"""
   .. automethod:: StrictSSDB.hrlist

   hkeys
   """""
   .. automethod:: StrictSSDB.hkeys

   hscan
   """""
   .. automethod:: StrictSSDB.hscan

   hrscan
   """"""
   .. automethod:: StrictSSDB.hrscan

   
   Zsets
   ^^^^^

   A sorted set in ssdb. It's contain keys with scores in ``zset`` 

   .. code-block:: python

      >>> from ssdb.client import SSDB
      >>> ssdb = SSDB()
      >>> ssdb.multi_zset('zset_1', a=30, b=20, c=100, d=1, e=64, f=-3,
      ...                 g=0)
      >>> ssdb.multi_zset('zset_2',
      ...                 key1=42,
      ...                 key2=314,
      ...                 key3=1,
      ...                 key4=256,
      ...                 key5=0,
      ...                 key6=-5
      ...                )

   zget
   """"
   .. automethod:: StrictSSDB.zget

   zset
   """"
   .. automethod:: StrictSSDB.zset

   zadd
   """"
   The same is `zset`_.

   zclear
   """"""
   .. automethod:: StrictSSDB.zclear

   zdel
   """"
   .. automethod:: StrictSSDB.zdel

   zremove
   """""""
   The same is `zdel`_.

   zset_exists
   """""""""""
   .. automethod:: StrictSSDB.zset_exists

   zexists
   """""""
   .. automethod:: StrictSSDB.zexists

   zincr
   """""
   .. automethod:: StrictSSDB.zincr

   zdecr
   """""
   .. automethod:: StrictSSDB.zdecr

   zsize
   """""
   .. automethod:: StrictSSDB.zsize

   zlen
   """"
   The same is `zsize`_.

   zcard
   """""
   The same is `zsize`_.

   multi_zget
   """"""""""
   .. automethod:: StrictSSDB.multi_zget

   zmget
   """""
   The same is `multi_zget`_.

   multi_zset
   """"""""""
   .. automethod:: StrictSSDB.multi_zset

   zmget
   """""
   The same is `multi_zset`_.

   multi_zdel
   """"""""""
   .. automethod:: StrictSSDB.multi_zdel

   zmdel
   """""
   The same is `multi_zdel`_.

   zlist
   """""
   .. automethod:: StrictSSDB.zlist

   zrlist
   """"""
   .. automethod:: StrictSSDB.zrlist

   zkeys
   """""
   .. automethod:: StrictSSDB.zkeys

   zscan
   """""
   .. automethod:: StrictSSDB.zscan

   zrscan
   """"""
   .. automethod:: StrictSSDB.zrscan

   zrank
   """""
   .. automethod:: StrictSSDB.zrank

   zrrank
   """"""
   .. automethod:: StrictSSDB.zrrank

   zrange
   """"""
   .. automethod:: StrictSSDB.zrange

   zrrange
   """""""
   .. automethod:: StrictSSDB.zrrange

   zcount
   """"""
   .. automethod:: StrictSSDB.zcount

   zsum
   """"
   .. automethod:: StrictSSDB.zsum

   zavg
   """"
   .. automethod:: StrictSSDB.zavg

   zremrangebyrank
   """""""""""""""
   .. automethod:: StrictSSDB.zremrangebyrank

   zremrangebyscore
   """"""""""""""""
   .. automethod:: StrictSSDB.zremrangebyscore


   Queue
   ^^^^^

   A queue in ssdb.

   .. code-block:: python

      >>> from ssdb.client import SSDB
      >>> ssdb = SSDB()
      >>> ssdb.qpush('queue_1', 'a', 'b', 'c', 'd', 'e', 'f', 'g')
      >>> ssdb.qpush('queue_2',
      ...            'test1',
      ...            'test2',
      ...            'test3',
      ...            'test4',
      ...            'test5',
      ...            'test6',
      ...            )

   qsize
   """""
   .. automethod:: StrictSSDB.qsize

   qlist
   """""
   .. automethod:: StrictSSDB.qlist

   qrlist
   """"""
   .. automethod:: StrictSSDB.qrlist

   qclear
   """"""
   .. automethod:: StrictSSDB.qclear

   qfront
   """"""
   .. automethod:: StrictSSDB.qfront

   qback
   """""
   .. automethod:: StrictSSDB.qback

   qget
   """"
   .. automethod:: StrictSSDB.qget

   qrange
   """"""
   .. automethod:: StrictSSDB.qrange

   qslice
   """"""
   .. automethod:: StrictSSDB.qslice

   qpush_front
   """""""""""
   .. automethod:: StrictSSDB.qpush_front

   qpush_back
   """"""""""
   .. automethod:: StrictSSDB.qpush_back

   qpush
   """""
   .. automethod:: StrictSSDB.qpush

   qpop_front
   """"""""""
   .. automethod:: StrictSSDB.qpop_front

   qpop
   """"
   .. automethod:: StrictSSDB.qpop

   qpop_back
   """""""""
   .. automethod:: StrictSSDB.qpop_back

   queue_exists
   """"""""""""
   .. automethod:: StrictSSDB.queue_exists


