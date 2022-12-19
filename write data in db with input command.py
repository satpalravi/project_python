#db connection and execution


import psycopg2
from config import config

def connect():
	""" Connect to the PostgreSQL database server """
	conn = None
	try:
		# read connection parameters
		params = config()

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
		
		#what data to insert in table
		ps_insert_date = """ INSERT INTO person(name, age, gender) VALUES(%s,%s,%s)"""
		name = input("Enter your name here : ")
		age = input("Enter your age here : ")
		gender = input("Enter your gender here (male/female): ")
		
		#collect data to insert in table from user
		record_to_insert = (name, age, gender)
		
		cur.execute(ps_insert_date, record_to_insert)
		
		conn.commit()
		count = cur.rowcount
		print(count, "Record inserted successfully into person table")
   
	# close the communication with the PostgreSQL
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')
        


if __name__ == '__main__':
	connect()
