import os
import redis

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = int(os.environ.get('DB_PORT', 6379))
r = redis.StrictRedis(DB_HOST, DB_PORT, 0)
