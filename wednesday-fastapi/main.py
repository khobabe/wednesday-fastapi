from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}/{roll}")
async def greet(name: str, roll:int):
    return {"message":f"hello,{name}! and your roll is {roll}! "}