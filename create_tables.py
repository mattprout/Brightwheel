import sqlite3
from sql_queries import drop_table_queries, create_table_queries


def create_tables(conn, cursor):
    
    for drop_table in drop_table_queries:
        cursor.execute(drop_table)
        conn.commit()
            
    for create_table in create_table_queries:
        cursor.execute(create_table)
        conn.commit()


def main():

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    create_tables(conn, cursor)
    
    conn.close()
    
    
if __name__ == "__main__":
    main()
