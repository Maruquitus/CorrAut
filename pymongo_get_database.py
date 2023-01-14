from pymongo import MongoClient
import urllib.parse
from pymongo.server_api import ServerApi
def conectar(usuário, senha):

    client = MongoClient(f"mongodb+srv://{usuário}:{urllib.parse.quote_plus(senha)}@corraut-db.7j5ar0f.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client.Database

    try:
        db.Collection.list_indexes()
        return db
    except:
        return "ERRO"
  
if __name__ == "__main__":   
    db = conectar