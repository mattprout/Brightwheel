# Analytics Engineer Exercise for Brightwheel
### Dec 28, 2020
  
# How to Install and Run
  
**Python libraries required:**  
sqlite3, pandas, requests  
  
**To run:**  
First create the staging tables: `python3 create_tables.py`  
Then perform the ETL: `python3 etl.py`  

Notes:
1. Currently the master 'Providers' table is recreated in create_tables.py.  With more time, this would be moved to a separate file so that it would be created once.  
2. The x_ca_omcc_providers.csv file needs to be in the same folder as etl.py

# Language and Frameworks

I chose to write the ETL script using Python, as that is one of the languages that I am most familiar with, and it has a large ecosystem of libraries for tasks such as text processing and connecting to databases.

For the database I chose to use Sqlite for several reasons.  First, the database can be created locally on my computer and does not require provisioning a database.  Second, using Sqlite allowed me to quickly iterate for this exercise and try different things quickly.  Third, the syntax is similar to PostgreSQL, so that it would likely run on a PostgreSQL db.

# Files
The deliverable files of the project are:  
`sql_queries.py`
`create_tables.py`
`etl.py`
[Not done: file to create the provider table once]
[Not done: notebook for analysis queries]

The following notebooks are included as an FYI and were for testing ideas before copying them to the deliverable files
TestProviders.ipynb  
TestEtl.ipynb  

# Design

The final Providers table includes all the fields in the x_ca_omcc_providers.csv CSV file, but also includes the email and owner name, which comes from the internal data source and external (web) source.  A primary key was created on the name and zip code, as it is assumed that there would not be two providers with the same name in the same zip code.  

The data from the CSV file is upserted into the Providers table, and update the address and phone number on a conflict, in case the user's phone or address changed.  

The internal JSON data is read into a staging table.  Although I did not make it this far, the plan was to update the Providers table joining on the provider name and phone number (the internal data does not provide a zip code).  The data that would be updated would be the owner and the email (only if it was NULL).  

I did not get to working on the ETL for the external (web) data, but that would have required navigating to pages at this URL and scraping the data with some library (Beautiful Soup?)

I did not get to creating a notebook for the analysis queries.  This would have connected to the database and performed the two queries to answer the questions:
1. How many Family Child Care Home providers are there in the dataset?
2. Which Zip code has the most providers?

# Additional Time
If I had additional time, I would have completed the ETL functionality (working on the external data source last), and created the analysis notebook.  I would have also provided better error handling, removed the hard-coded strings for the source data, and cleaned up the normalization code.
