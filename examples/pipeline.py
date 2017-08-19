from cssdbpy import Connection

def example_pipeline():
	conn = Connection("127.0.0.1", 8888)
	for result in conn.pipeline(("hset","test","one",150,),("hexists","test","one",),("hget","test","one",)):
		print(result)



if __name__ == '__main__':
	example_pipeline()
