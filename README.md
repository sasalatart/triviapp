# Triviapp

> My first Python Flask application

### Setup

##### Development

1. Make sure that at least [Python 3.4.3](https://www.python.org/downloads/) and
[redis](http://redis.io/download) are installed.
2. Clone and cd into this repository
3. Set the environment variables:
  - SECRET_KEY ('napoleon' should work)
  - SERVER_HOST ('localhost' should work)
  - SERVER_PORT ('5000' should work)
  - TRIVIAPP_DB_HOST ('localhost' should work)
  - TRIVIAPP_DB_PORT ('6379' should work)
  - TRIVIAPP_DB_NAME ('0' should work)
4. Run `pip install -r requirements.txt`
5. Open another shell instance and run `redis-server`
6. Run `python app.py`

In order to populate the initial database, you may run `python seed.py`.

##### Docker

```sh
# Build
$ docker-compose build

# Run
$ docker-compose up -d

# Seed
$ docker-compose run web python seed.py
```

The server's machine should now be redirecting its port 80 to the container's
port 5000. Remember to set the appropriate environment variables if the server
is being shared with other applications. If that is not the case, the default
values should be ok.

To stop:
```sh
$ docker-compose stop
```
