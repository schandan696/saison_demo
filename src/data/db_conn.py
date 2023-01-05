import psycopg2
from psycopg2 import pool
from config.config import config

def getConnectionPool():
    try:
        db_config = config()
        postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20, **db_config)
        if (postgreSQL_pool):
            print("Connection pool created successfully")
        return postgreSQL_pool
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if postgreSQL_pool:
            postgreSQL_pool.closeall
        print("PostgreSQL connection pool is closed")