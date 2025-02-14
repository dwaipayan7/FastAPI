from fastapi import FastAPI 


app = FastAPI()


@app.get("/blog")
def index(limit, published: bool):

    return published

    if published:
        return {'data': f'{limit} blogs published from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}




@app.get('/blog/unpublished')
def unpublished():
    return {"data": "all unpublished blogs"}



@app.get('/blog/{id}')
def fetch(id: int): #define type
    return {'data': id}    


@app.get('/blog/{id}/comments')
def fetch_comments(id):
    return {'data': {'1','2'}}