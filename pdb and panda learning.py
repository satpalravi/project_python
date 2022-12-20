#db connection and execution


import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
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
		print("The Requesed info is below")
		print("")
		cur.execute("""
              
              select count(distinct(username)) as "No. of Players",difficulty,
              sum(most_friendly_fire) as "Total Friendly Fires"
              from player_stats 
              group by difficulty
              order by difficulty asc
              
              """)
		data = cur.fetchall()

#read columns of the table for panda dataframe starting index 0
		cols = []
		for col in cur.description:
			cols.append(col[0])

#make panda data frame using the sql data and column names
		df = pd.DataFrame(data=data, columns=cols)
		print(df)

#display the data in the matplotlib chart
		df.plot(kind="bar", x="difficulty", y="No. of Players")
		plt.show()


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
