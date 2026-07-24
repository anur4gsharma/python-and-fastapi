from fastapi import FastAPI
import fastapi

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Hello motherfucking backend!"}

@app.get("/about")
def abt():
    return {"dev" : "that's me", "remark" : "bitch"}

@app.get("/health")
def hlth():
    return {"message" : "Yep health is fine ig"}