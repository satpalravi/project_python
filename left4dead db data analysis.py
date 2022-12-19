#db connection and execution


import psycopg2
from dbconnector import dbconnect

def connect():
	""" Connect to the PostgreSQL database server """
	conn = None
	try:
		# read connection parameters
		params = dbconnect()

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)
		
		# create a cursor
		cur = conn.cursor()
		
	    # execute a statement
		print('PostgreSQL database version:')
		cur.execute('SELECT version()')
		
		# display the PostgreSQL database server version
		db_version = cur.fetchone()
		print(db_version)
		print("")
        
		#pull data from db for analysis
		print("The Requesed data is below")
		print("")
		cur.execute("select * from player_stats")
		data = cur.fetchone()
		print(data)
		
   
	# close the communication with the PostgreSQL
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print("")
			print('Database connection closed.')
        


if __name__ == '__main__':
	connect()
