from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymongo
import traceback
from string import capwords


ícones = {
    "Turismo":"fa-solid fa-plane",
    "Enfermagem":"fa-solid fa-heart-pulse",
    "Informática":"fa-solid fa-computer",
    "Agroindústria":"fa-solid fa-tractor",
    "Vestuário": "fa-solid fa-shirt"
}

def formatarDict(dict):
    for k in dict.keys():
        if isinstance(dict[k], str) and k != "ObjectId":
            dict[k] = capwords(dict[k])
    return dict

def formatarArray(array):
    a = array
    ind = 0
    for i in array:
        if isinstance(i, str):
            a[ind] = capwords(i)
        ind += 1
    return a


def redirect(request):
    return HttpResponseRedirect(f'/login/')

def login(request):
    if request.method == 'GET':
        if "erro" in request.GET.keys():
            erros = {
                "1": "Credenciais incorretas, verifique-as e tente novamente.",
                "2": "IP bloqueado, fale com um administrador.",
                "3": "Conecte-se à internet e tente novamente.",
                "4": "Algo deu errado, tente novamente.",
                "5": "Usuário / senha não podem estar vazios!"
            }
            erro = erros[request.GET["erro"]]
            return render(request, 'login.html', {"msgErro":erro})
        
        
    return render(request, 'login.html')

def cadgab(request):
    global turmas
    if request.method == 'GET':
        try:
            t = int(request.GET["turma"])
            t = turmas[t]
            t = formatarDict(t)
            if "questoes" in request.GET.keys():
                quant = int(request.GET["questoes"])
                return render(request, "cadgab.html", {'questões':range(1, quant+1), 'quant':quant, 'curso':t['curso'], 'série':t['série'], 'ícone': ícones[t['curso']]})
            else:
                print(ícones[t['curso']])
                return render(request, "cadgab.html", {'questões':range(1, 11), 'quant':10, 'curso':t['curso'], 'série':t['série'], 'ícone': ícones[t['curso']]})
        except Exception as e:
            print(traceback.format_exc())
            return HttpResponseRedirect(f'/login/?erro=4')

def turmasPag(request):
    global db, usuario, turmas
    if request.method == 'GET':
        try:
            type(usuario)
            usuárioDados = db.Usuários.find({"usuário":usuario})[0]
            turmas = []
            ind = 0
            if usuárioDados['turmas'] != ["*"]:
                for tt in db.Turmas.find().sort([("série", pymongo.ASCENDING)]):
                    t = formatarDict(tt)
                    print(t)
                    tAtual = f"{t['curso']} {t['série']}".upper()
                    print(tAtual, usuárioDados['turmas'])
                    if tAtual in usuárioDados['turmas']:
                        turmas.append({"curso": t['curso'], "série": t['série'], "ícone":ícones[t['curso']], "add": "enabled", "id":ind})
                    else:
                        turmas.append({"curso": t['curso'], "série": t['série'], "ícone":ícones[t['curso']], "add": "disabled", "id":ind})
                    ind += 1
            else:
                for tt in db.Turmas.find().sort([("série", pymongo.ASCENDING)]):
                    t = formatarDict(tt)
                    turmas.append({"curso": t['curso'], "série": t['série'], "ícone":ícones[t['curso']],"add": "", "id":ind})
                    ind += 1

            return render(request, "turmas.html", {'usuario':usuario, '1º':turmas[0:4], "2º":turmas[4:8], "3º":turmas[8:12]})
        except Exception as e:
            print(traceback.format_exc())
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