from typing import Union

from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host = "redis-15998.c264.ap-south-1-1.ec2.redns.redis-cloud.com",
    port = 15998,
    password = "yeRdB7kBYnP6eeG45OksdfLh9iJLlDhL",
    decode_responses = True
)

class Product:
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get('/products')
def allProducts():
    return []