from fastapi import FastAPI

app = FastAPI()


@app.get('/login')
def root():
    return {"message": "Hello World"}
