from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')
def index(limit=10, published:bool = True, sort: Optional[str] = None):
    # only get (if limit=10) 10 published blogs
    if published:
        return {'data': f'{limit} of published blogs from db'}
    else:
        return {'data': f'{limit} of blogs from database'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch commnts of blog with id = id
    return {'data': {'comment nr 1', 'comment nr 2'}}
