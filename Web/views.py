from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymongo


def redirect(request):
    return HttpResponseRedirect(f'/login/')

def login(request):
    if request.method == 'GET':
        if "erro" in request.GET.keys():
            erros = {
                "1": "Credenciais incorretas, verifique-as e tente novamente.",
                "2": "IP não adicionado, fale com um administrador.",
                "3": "Conecte-se à internet e tente novamente.",
                "4": "Algo deu errado, tente novamente."
            }
            erro = erros[request.GET["erro"]]
            return render(request, 'login.html', {"msgErro":erro})
        
        
    return render(request, 'login.html')

def turmas(request):
    global db, usuario
    try:
        type(usuario)
        usuárioDados = db.Usuários.find({"usuário":usuario})[0]
        turmas = []
        if usuárioDados['turmas'] != ["*"]:
            for t in db.Turmas.find().sort([("série", pymongo.ASCENDING)]):
                tAtual = f"{t['curso']} {t['série']}"
                if tAtual in usuárioDados['turmas']:
                    turmas.append({"curso": t['curso'], "série": t['série'], "add": "enabled"})
                else:
                    turmas.append({"curso": t['curso'], "série": t['série'], "add": "disabled"})
        else:
            for t in db.Turmas.find().sort([("série", pymongo.ASCENDING)]):
                turmas.append({"curso": t['curso'], "série": t['série'], "add": ""})

        return render(request, "turmas.html", {'usuario':usuario, '1º':turmas[0:4], "2º":turmas[4:8], "3º":turmas[8:12]})
    except Exception as e:
        print(repr(e))
        return HttpResponseRedirect(f'/login/?erro=4')

def checar(request):
    global db, usuario
    if request.method == 'POST' and 'usuário' in request.POST:
        usuario = request.POST["usuário"]
        senha = request.POST["senha"]

        import database as d
        db = d.conectar(usuario, senha)
        if not isinstance(db, str):
            return HttpResponseRedirect('/turmas/')
        else:
            erro = db.replace("ERRO: ", "")
            db = None
            return HttpResponseRedirect(f'/login/?erro={erro}')
            
    
    return render(request, 'login.html')