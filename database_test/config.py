#!/usr/bin/python
import psycopg2
from configparser import ConfigParser

def write_blob(part_id, path_to_file, file_extension):
    """ insert a BLOB into a table """
    conn = None
    try:
        # read data from a picture
        drawing = open(path_to_file, 'rb').read()
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO video(vid_id,vid_name) "
                    "VALUES(%s,%s)",
                    (part_id, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.commit()
        print('done')
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
# def create_tables():
#     """ create tables in the PostgreSQL database"""
#     commands = (
#         """ CREATE TABLE video (
#                 vid_id SERIAL PRIMARY KEY,
#                 vid_name BYTEA NOT NULL
#                 )
#         """,)
#     conn = None
#     try:
#         # read the connection parameters
#         params = config()
#         # connect to the PostgreSQL server
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         # create table one by one
#         for command in commands:
#             cur.execute(command)
#         # close communication with the PostgreSQL database server
#         cur.close()
#         # commit the changes
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

def read_blob():
    # """ read BLOB data from a table """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(""" SELECT *
                        FROM video"""
                        )
 
        blob = cur.fetchone()
        open('videos/' + 'images' + 'hello' + '.mov', 'wb').write(blob[1])
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
     read_blob()

