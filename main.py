from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/random_macadress/")
async def random_macadress():
    mac_list = []
    hex_char = '0123456789ABCDEF'
    for x in range(6):
        r1 = random.choice(hex_char)   
        r2 = random.choice(hex_char)
        r3 = r1+r2
        mac_list.append(r3)
    final_mac = '-'.join(mac_list)
    return(final_mac)
    