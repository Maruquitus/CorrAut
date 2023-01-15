from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError, ConfigurationError
import urllib.parse
from pymongo.server_api import ServerApi
import urllib.request
def testarInternet(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def conectar(usuário, senha):
    global db
    temInternet = testarInternet()

    if temInternet:
        client = MongoClient(f"mongodb+srv://{usuário}:{urllib.parse.quote_plus(senha)}@corraut-db.7j5ar0f.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
        db = client.Database

        "OperationFailure" #Credenciais erradas
        "ServerSelectionTimeoutError" #IP não adicionado
        #"ConfigurationError" #Sem internet

        try:
            print(db.Alunos.list_indexes())
            return db
        except OperationFailure:
            return "ERRO: 1"
        except ServerSelectionTimeoutError:
            return "ERRO: 2"
        #except ConfigurationError:
            #return "ERRO: Sem internet"
    else:
        return "ERRO: 3"


  
if __name__ == "__main__":   
    db = conectar

def novoAluno(nome, turma):
    global db
    try:
        print(db)
    except:
        print("Conexão não encontrada, faça login para prosseguir")
        usuário = input("Usuário >>> ")
        senha = input("Senha >>> ")
        db = conectar(usuário, senha)
    db.Alunos.insert_one({"nome":nome, "turma":turma, "histórico": []})

def novoUsuario(usuario):
    global db
    try:
        print(db)
    except:
        print("Conexão não encontrada, faça login para prosseguir")
        usuário = input("Usuário >>> ")
        senha = input("Senha >>> ")
        db = conectar(usuário, senha)
    db.Usuários.insert_one({"usuário":usuario, "turmas": []})


def novaTurma(curso, série, quantidadeAlunos):
    global db
    try:
        print(db)
    except:
        print("Conexão não encontrada, faça login para prosseguir")
        usuário = input("Usuário >>> ")
        senha = input("Senha >>> ")
        db = conectar(usuário, senha)
    db.Turmas.insert_one({"curso":curso, "série":série, "quantidadeAlunos": quantidadeAlunos})