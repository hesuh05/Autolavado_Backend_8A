from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def root_function():
    return {"message":"Welcome!"}
