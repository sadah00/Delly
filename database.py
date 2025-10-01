import select
import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="kimysada6",dbname="delly")
cur=conn.cursor()