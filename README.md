# Triviapp

> Trivia application built with Python Flask.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)](sasalatart/triviapp)
[![](https://images.microbadger.com/badges/version/sasalatart/triviapp.svg)](https://microbadger.com/images/sasalatart/triviapp)
[![](https://images.microbadger.com/badges/image/sasalatart/triviapp.svg)](https://microbadger.com/images/sasalatart/triviapp)
[![Code Climate](https://codeclimate.com/github/sasalatart/triviapp/badges/gpa.svg)](https://codeclimate.com/github/sasalatart/triviapp)

### Setup

#### Development

1. Make sure that at least [Python 3.4.3](https://www.python.org/downloads/) and [redis](http://redis.io/download) are installed.
2. Clone and cd into this repository
3. Set the environment variables:
  - HOST ('0.0.0.0' by default)
  - PORT ('5000' by default)
  - DB_HOST ('localhost' should work)
  - DB_PORT ('6379' by default)
  - DB_NAME ('0' by default)
4. Run `pip install -r requirements.txt`
5. Open another shell instance and run `redis-server`
6. Run `python app.py`

In order to populate the initial database, you may run `python seed.py`.

#### Docker

```sh
# Pull and run the application and redis
$ docker run -d --name=redis_db redis:3.0

$ docker run -d --name=triviapp -p 80:5000 --link=redis_db:redis_db sasalatart/triviapp

# Setup the database
$ docker exec triviapp python db/seed.py
```

The server's machine should now be redirecting its port 80 to the container's port 5000.
