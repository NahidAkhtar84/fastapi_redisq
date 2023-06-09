from os import environ
from rq import Queue
from redis.client import Redis
from redis.exceptions import RedisError

from core.log import logger


class RedisConfig:
    def __init__(self, config=dict()):
        self.__config = config

    def get(self, key):
        return self.__config.get(key)

    def set(self, key, value):
        self.__config[key] = value


class RedisClient:
    def __init__(self, host=environ.get("REDIS_HOSTNAME", "localhost"), port=6379):
        self.__host = host
        self.__port = port
        self.__client = Redis(host, port, retry_on_timeout=True)

    def queue(self, queue_name):
        return Queue(queue_name, connection=self.__client)

    def publish(self, channel, message):
        try:
            self.__client.xadd(channel, message)
        except RedisError:
            logger.error("Failed to publish message to channel")

