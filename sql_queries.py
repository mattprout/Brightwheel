

# Drop tables
drop_providers = "DROP TABLE IF EXISTS Providers;"
drop_csv = "DROP TABLE IF EXISTS CSVSource;"
drop_internal = "DROP TABLE IF EXISTS InternalSource;"

drop_table_queries = [drop_providers, drop_csv, drop_internal]

# Create tables
create_providers = """
CREATE TABLE Providers (
   Name TEXT,
   Type TEXT,
   Address TEXT,
   City TEXT,
   State VARCHAR(2),
   Zip INT,
   Phone INT,
   Owner TEXT,
   Email TEXT,
   PRIMARY KEY (Name, Zip)
);"""

create_csv = """
CREATE TABLE CSVSource (
   Name TEXT,
   Type TEXT,
   Address TEXT,
   City TEXT,
   State VARCHAR(2),
   Zip INT,
   Phone INT
);"""

create_internal_table = """
CREATE TABLE InternalSource (
   ID TEXT,
   Name TEXT,
   Phone INT,
   Email TEXT,
   Owner TEXT
);
"""

create_table_queries = [create_providers, create_csv, create_internal_table]

# Insert statements
insert_csv = """
INSERT INTO Providers (Name, Type, Address, City, State, Zip, Phone)
VALUES(?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(Name, Zip) DO UPDATE SET
Address = excluded.Address, Phone = excluded.Phone;
"""

insert_internal = """
INSERT INTO InternalSource (ID, Name, Phone, Email, Owner)
VALUES(?, ?, ?, ?, ?);
"""

