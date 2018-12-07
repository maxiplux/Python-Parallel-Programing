#"data.csv"

DATA_PATH = "datasimple.csv"  # this the file to load on db
PART_OF_DATA = 3 # here you need work with the best settings to your problem
POOL_PROCESS=10 # when you have many data this value , reduce time on process each line and write it on db.
CREATE_TABLES = True # if you like that pony make a table
# the next lines  are to db , but you can change by any db  that work using schme client and server .
# this program not work with sqlite , because we have a lot agent writting data on db.
PROVIDER = "postgres"
DB_SCHEME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
