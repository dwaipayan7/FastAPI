from fastapi import FastAPI 


app = FastAPI()


@app.get("/")
def index():
    return {'data': 'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {"data": "all unpublished blogs"}



@app.get('/blog/{id}')
def fetch(id: int): #define type
    return {'data': id}    


@app.get('/blog/{id}/comments')
def fetch_comments(id):
    return {'data': {'1','2'}}