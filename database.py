from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError, InvalidURI, ConfigurationError
import urllib.parse
from pymongo.server_api import ServerApi
import urllib.request
import bcrypt

def testarInternet(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def conectar(usuário, senha=-1, si=-1):
    global db
    temInternet = testarInternet()

    if temInternet:
        try:
            try:
                print(db)
            except:
                if usuário != "ADMIN":
                    uri = f"mongodb+srv://corraut-db.7j5ar0f.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
                    client = MongoClient(uri,
                            tls=True,
                            tlsCertificateKeyFile='auth.pem',
                            server_api=ServerApi('1'))
                else:
                    client = MongoClient(f"mongodb+srv://{usuário}:{urllib.parse.quote_plus(senha)}@corraut-db.7j5ar0f.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
                db = client.Database

            "OperationFailure" #Credenciais erradas
            "ServerSelectionTimeoutError" #IP não adicionado
            #"ConfigurationError" #Sem internet

            if usuário != "ADMIN" and senha != -1:
                senha = senha.encode('utf-8')
                print(db.Usuários.find({"usuário":usuário}))
                try:
                    if not bcrypt.checkpw(senha, db.Usuários.find({"usuário":usuário})[0]['senha']):
                        return "ERRO: 1"
                except:
                    return "ERRO: 1"
            else:
                if db.Usuários.find({"usuário":usuário})[0]['sessãoAtual'] != si:
                    return "ERRO: 6"

            try:
                print(db.Alunos.list_indexes())
                return db
            except OperationFailure:
                return "ERRO: 1"
            except ServerSelectionTimeoutError:
                return "ERRO: 2"
            except InvalidURI:
                return "ERRO: 5"
        except InvalidURI:
            return "ERRO: 5"
        except ConfigurationError:
            return "ERRO: 5"
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
    db.Alunos.insert_one({"nome":nome.upper(), "turma":turma.upper(), "histórico": {"1º":{}, "2º":{}, "3º": {}}})

def novoUsuario(usuario, senha):
    global db
    try:
        print(db)
    except:
        print("Conexão não encontrada, faça login para prosseguir")
        usuário = input("Usuário >>> ")
        senha = input("Senha >>> ")
        db = conectar(usuário, senha)

    senha = senha.encode('utf-8')
    hashed = bcrypt.hashpw(senha, bcrypt.gensalt(10)) 
    
    db.Usuários.insert_one({"usuário":usuario.upper(), "turmas": [], "senha":hashed, "matérias": [], "sessãoAtual":b""})

def atualizarUsuario(usuario, atualizar, valor):
    global db
    db.Usuários.update_one({"usuário":usuario}, {"$set":{atualizar:valor}})


def novaTurma(curso, série, quantidadeAlunos):
    global db
    try:
        print(db)
    except:
        print("Conexão não encontrada, faça login para prosseguir")
        usuário = input("Usuário >>> ")
        senha = input("Senha >>> ")
        db = conectar(usuário, senha)
    db.Turmas.insert_one({"curso":curso.upper(), "série":série.upper(), "quantidadeAlunos": quantidadeAlunos})

def atualizarTurma(turma, atualizar, valor):
    t = turma.split()
    db.Usuário.update_one({"curso":t[0], "série":int(t[1][0])}, {"$set":{atualizar:valor}})

def atualizarNota(nome, ano, matéria, período, nota):
    aluno = db.Alunos.find({"nome":nome.upper()})[0]
    hist = aluno['histórico']
    try:
        aluno['histórico'][ano][matéria][período]
        hist[ano][matéria][período] = nota

        db.Alunos.update_one({"nome":nome.upper()}, {"$set":{"histórico":hist}})
    except Exception as e:
        hist[ano][matéria] = {"1º":-1, "2º":-1, "3º":-1, "4º":-1}
        db.Alunos.update_one({"nome":nome.upper()}, {"$set":{"histórico":hist}})
        atualizarNota(nome, ano, matéria, período, nota)

def calcularMediaTurma(turma, anoPesquisa, matéria):
    global db

    médias = []
    
    for período in ["1º", "2º", "3º", "4º"]:
        alunos = db.Alunos.find({"turma":turma})
        ano = anoPesquisa
        alunosContabilizados = 0
        soma = 0
        for aluno in alunos:
            nota = aluno["histórico"][ano][matéria][período]
            if nota != -1:
                soma += aluno["histórico"][ano][matéria][período]
                alunosContabilizados += 1
        try:
            média = soma/alunosContabilizados
            médias.append(média)
        except:
            médias.append(0)

    return médias

    

    