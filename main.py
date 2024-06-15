from typing import Union

from fastapi import FastAPI
from config import db

app = FastAPI()


# Esto es un endpoint o ruta
@app.get("/")
def read_root():
    return {"Hello": "World"}

# obtener todas las noticias
@app.get("/news")
def get_news():
    articles = db.get("news")
    return {"news": articles}

# obtener noticia por id
@app.get("/news/{article_id}")
def get_news_by_id(article_id):
    articles = db.get("news")
    article = None
    

    for art in articles: 
        if int(art.get("id")) == int(article_id):
            article = art
            break

    return {
        "article": article
    }
        
# crear noticias o articulos

# editar noticia por id

# eliminar noticie por id 
