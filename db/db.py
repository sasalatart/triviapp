import os
import redis


DB_URL = os.environ.get('REDIS_URL', 0)
DB_HOST = os.environ.get('DB_HOST', 'redis_db')
DB_PORT = int(os.environ.get('DB_PORT', 6379))
DB_NAME = int(os.environ.get('DB_NAME', 0))

if DB_URL != 0:
    r = redis.from_url(DB_URL)
else:
    r = redis.StrictRedis(DB_HOST, DB_PORT, DB_NAME)
