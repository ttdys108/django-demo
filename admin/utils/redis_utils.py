import redis

pool = redis.ConnectionPool(host='121.36.137.124', port=6379, max_connections=10, password='tyuiop')
redisTemplate = redis.Redis(connection_pool=pool)


