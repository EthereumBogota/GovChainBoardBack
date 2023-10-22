# Commands:

```
docker build -t govchainboard:latest .
docker run -p 8080:80 -v "$(pwd)":/code -it govchainboard:latest
```