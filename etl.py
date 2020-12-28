import sqlite3
from sql_queries import insert_csv, insert_internal
import pandas as pd
import requests
import re


# TODO
csv_file = 'F:/Brightwheel/x_ca_omcc_providers.csv'


def etl_csv(conn, cursor):
    
    df = pd.read_csv(csv_file, header=None)
    df.columns = ['Name', 'Type', 'Address', 'City', 'State', 'Zip', 'Phone']
    
    # Change columns to string
    # TODO: see how to do this in read_csv()
    
    df['Name'] = df['Name'].astype(str)
    df['Type'] = df['Type'].astype(str)
    df['Address'] = df['Address'].astype(str)
    df['City'] = df['City'].astype(str)
    df['State'] = df['State'].astype(str)
    
    for idx, row in df.iterrows():
        cursor.execute(insert_csv, (row['Name'].upper(), row['Type'].upper(), row['Address'].upper(), row['City'].upper(), row['State'].upper(), int(row['Zip']), int(row['Phone'])))
        
    conn.commit()

        
# TODO
internal_data_source = 'https://bw-interviews.herokuapp.com/data/providers'
        
def phoneNormalize(phone_number):
    return re.sub("[^0-9]", "", phone_number)

def toUpperNormalize(value):
    if value:
        return value.upper()
    return value
    
def etl_internal(conn, cursor):
    
    response = requests.get(internal_data_source)
    
    if response.status_code == 200:
        
        json_output = response.json()
        
        for row in json_output['providers']:
            cursor.execute(insert_internal, (toUpperNormalize(row['id']), toUpperNormalize(row['provider_name']), phoneNormalize(row['phone']), toUpperNormalize(row['email']), toUpperNormalize(row['owner_name'])))
    
        conn.commit()
        
        # TODO
        # Need to update Providers with data from InternalSource staging table
 
    else:
        print('Could not open the internal data source')


def main():

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    etl_csv(conn, cursor)

    conn.close()
    
    
if __name__ == "__main__":
    main()
