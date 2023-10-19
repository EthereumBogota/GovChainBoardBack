Installing psql

```
psqlsudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

Connecting to Database
```
psql  --host=<DB instance endpoint>  --port=<port>  --username=<master username> --password --dbname=<database name> 
```
psql  --host=govchainboard2.ckody2xernst.us-east-2.rds.amazonaws.com  --port=5432 --username=x --password --dbname=x



go install github.com/filecoin-project/lassie/cmd/lassie@latest
lassi





basin publication create  --dburi postgresql://govchainboard2:govchainboard2@govchainboard2.ckody2xernst.us-east-2.rds.amazonaws.com:5432/govchainboard2 --address 0x2A96F741808A0CD1650A8836f309eE9443756AeF govchainboard2.users




/home/codespace/.basin/config.yaml