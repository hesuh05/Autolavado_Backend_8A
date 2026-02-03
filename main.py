"""
    Docstring para main
"""

from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def root_function():
    """
        Docstring para root_function
    """
    return {"message":"Welcome!"}
