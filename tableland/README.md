# Basin-Cli
Basin-cli is the Tableland suggested option that allows to continuously publish data from your database to the Tableland network.
[Repository](https://github.com/tablelandnetwork/basin-cli)
[Guides](https://textile.notion.site/Tableland-Basin-Guide-20a27d0b147640b8a5b2fac0e55e1068?pvs=4)


# Create a publication

``` 
basin publication create  --dburi postgresql://<USERNAME>:<PASSWORD>@govchainboard2.ckody2xernst.us-east-2.rds.amazonaws.com:5432/govchainboard2 --address 0x2A96F741808A0CD1650A8836f309eE9443756AeF govchainboard2.users
``` 

# Start replicating a publication

Use `basin publication start` to start a daemon that will continuously push changes to the underlying table/view to the network.

```bash
basin publication start --private-key [WALLET_PRIVATE_KEY] govchainboard2.users
```

# PSQL
After we create the publication we need a way to connect to the database. For simplicity the example initially used PSQL.

Psql is a terminal-based front-end to PostgreSQL. It enables you to type in queries interactively, issue them to PostgreSQL, and see the query results.

### Installing psql

```
psqlsudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

### Connecting to Database using PSQL
```
psql  --host=<DB instance endpoint>  --port=<port>  --username=<master username> --password --dbname=<database name> 
```

# Check the Basin-Cli configuration file

``` 
/home/codespace/.basin/config.yaml
``` 


# List tables
``` 
basin publication list --address 0x3169a3375044BD54090EEE52a070896e414C5447 
```
govchainboard2.users


# Fetch events
```
basin publication deals --publication govchainboard2.users --latest 5
```
+----------+-------------------------------------------+-------------------------------------------------------------+
|    ID    |               SELECTOR PATH               |                             CID                             |
+----------+-------------------------------------------+-------------------------------------------------------------+
| 58607957 | Links/59/Hash/Links/33/Hash/Links/1/Hash  | bafybeic3rjdwkeeskbp2igl6hq6pmr2sw3pknex3rijly4cjs6gnkzkibe |
| 58629019 | Links/59/Hash/Links/33/Hash/Links/1/Hash  | bafybeic3rjdwkeeskbp2igl6hq6pmr2sw3pknex3rijly4cjs6gnkzkibe |
| 58607957 | Links/231/Hash/Links/46/Hash/Links/0/Hash | bafybeibhfyjkhp4r3iiucyk7kzvghjudyomu6lzlf66lkcs623k4xiobwu |
| 58629019 | Links/231/Hash/Links/46/Hash/Links/0/Hash | bafybeibhfyjkhp4r3iiucyk7kzvghjudyomu6lzlf66lkcs623k4xiobwu |
+----------+-------------------------------------------+-------------------------------------------------------------+


# Fetching the data and saving it on a .parquet file (Useful compression format)
```
lassie fetch -o - bafybeibhfyjkhp4r3iiucyk7kzvghjudyomu6lzlf66lkcs623k4xiobwu | car extract
```

# Read it on a python Dataframe
```python
import pandas as pd
pd.read_parquet(
    'govchainboard2/users/export178e1ed3421686800000000000000001-n908517711092285441.0.parquet'
    , engine='pyarrow'
    )
```

Check the **connecting_db.ipynb** notebook.

    id	name	email

0	4	Ejemplo Usuario 4	usuario4@example.com

1	5	Ejemplo Usuario 3	usuario3@example.com

2	6	Ejemplo Usuario 5	usuario5@example.com

3	7	Ejemplo Usuario 6	usuario6@example.com

4	8	Ejemplo Usuario 7	usuario7@example.com