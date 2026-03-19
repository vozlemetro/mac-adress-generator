from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/random_macadress/{counter}")
async def random_macadress(counter):
    amount = int(counter)
    
    mac_pieces = []
    mac_finals = []
    hex_char = '0123456789ABCDEF'
    for y in range(amount):
        mac_list = []
        for x in range(6):
            r1 = random.choice(hex_char)   
            r2 = random.choice(hex_char)
            r3 = r1+r2
            mac_list.append(r3)
        mac_pieces = '-'.join(mac_list)
        mac_finals.append(mac_pieces)
    return(mac_finals)
    