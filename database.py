import select
import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="kimysada6",dbname="delly")
cur=conn.cursor()

def insert_user(user_details):
    cur.execute(f"INSERT INTO users (name,email,phone_number,password) VALUES{user_details}")
    conn.commit()


def check_user(email):
    cur.execute("select * from users where email = %s",(email,))
    user = cur.fetchone()   
    return user