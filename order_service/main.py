from fastapi import FastAPI
import redis
import os

app = FastAPI()
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, db=0)

@app.post("/order")
def create_order(item: str):
    r.lpush("orders", item)
    return {"status": "ok", "message": f"Заказ на '{item}' принят и отправлен на кухню!"}