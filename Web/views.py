from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymongo
import traceback
from string import capwords
import database as d
import secrets


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

def erro(e):
    return HttpResponseRedirect(f'/login/?erro={e}')

def val(request):
    global db
    
    usuario = request.COOKIES["usuario"]

    #Checar se o cookie do sessionID não expirou 
    try:
        sessionID = request.COOKIES["sessionid"]
    except:
        return 6
    
    #Checar se o sessionID bate
    try:
        if db.Usuários.find({"usuário":usuario})[0]['sessãoAtual'] != sessionID:
            return 6
    except:
        db = d.conectar(usuario, si=sessionID)
        if isinstance(db, str):
            return int(db.replace("ERRO: ", ""))

    #Se nada der errado, retornar informações
    return usuario

def redirect():
    return HttpResponseRedirect(f'/login/')

def login(request):
    if request.method == 'GET':
        if "erro" in request.GET.keys():
            erros = {
                "1": "Credenciais incorretas, verifique-as e tente novamente.",
                "2": "IP bloqueado, fale com um administrador.",
                "3": "Conecte-se à internet e tente novamente.",
                "4": "Algo deu errado, tente novamente.",
                "5": "Usuário / senha não podem estar vazios!",
                "6": "Sua sessão expirou, entre novamente."
            }
            erro = erros[request.GET["erro"]]
            return render(request, 'login.html', {"msgErro":erro})
        
        
    return render(request, 'login.html')

def dashboard(request):
    global db
    
    #Validar o request (checar db e sessionID)
    v = val(request)
    if isinstance(v, int):    return v
    else:   usuario = v

    if request.method == 'GET':
        k = request.COOKIES.keys()
        try:
            turmas = calcularTurmas(db, usuario)
            if "turma" in k:
                turma = turmas[int(request.COOKIES["turma"])]
                cursoturma = turma["curso"]
                serieturma = turma["série"]
                try: 
                    #request.COOKIES["materia"]
                    #CONSIDERANDO SÓ NOTAS DO 1º, MUDAR DEPOIS
                    #dados = d.calcularMediaTurma(f"{cursoturma} {serieturma}º ANO", {serieturma}, request.COOKIES["materia"]) 
                    dados = d.calcularMediaTurma(f"{cursoturma.upper()} {serieturma}º ANO", "1º", "Matemática") 
                except:
                    dados = [0, 0, 0, 0]
                return render(request, 'dashboard.html', {"dados":dados, "acertosClass":"chartAcertos-container" if "ultimaAvaliacao" in k and dados != [0, 0, 0, 0] else "chartAcertosDisabled-container", "turma":f"{cursoturma} {serieturma}º Ano"})
            else:
                return render(request, 'dashboard.html', {"dados":[20, 45, 49, 20], "labels":[f"{n}º" for n in range(1, 10+1)], "acertosClass":"chartAcertosDisabled-container", "turma":f"{cursoturma} {serieturma}º Ano"})
        except:
            return erro(4)
            
"""
def setCookie(request):
    response = HttpResponse("Cookie Setado")
    k = list(request.GET.keys())
    if len(k) > 0:
        response.set_cookie(k[0], request.GET[k[0]])
    return response  
"""
    
def cadgab(request):
    global db
    #Validar o request (checar db e sessionID)
    v = val(request)
    if isinstance(v, int):    return v
    else:   usuario = v

    turmas = calcularTurmas(db, usuario)

    if request.method == 'GET':
        try:
            t = formatarDict(turmas[int(request.COOKIES['turma'])])
            quant = int(request.COOKIES['questoes']) if "questoes" in request.COOKIES.keys() else 10
            return render(request, "cadgab.html", {'questões':range(1, quant+1), 'quant':quant, 'curso':t['curso'], 'série':t['série'], 'ícone': ícones[t['curso']]})
        except:
            return erro(4)

def calcularTurmas(db, usuario):
    turmas = []
    ind = 0
    usuárioDados = db.Usuários.find({"usuário":usuario})[0]
    for tt in db.Turmas.find().sort([("série", pymongo.ASCENDING)]):
        t = formatarDict(tt)
        tAtual = f"{t['curso']} {t['série']}".upper()
        turmas.append({"curso": t['curso'], "série": t['série'], "ícone":ícones[t['curso']], "add": "enabled" if tAtual in usuárioDados['turmas'] or usuárioDados['turmas'] == ["*"] else "disabled", "id":ind})
        ind += 1
    return turmas

def turmasPag(request):
    global db
    #Validar o request (checar db e sessionID)
    v = val(request)
    if isinstance(v, int):    return v
    else:   usuario = v
    
    if request.method == 'GET':
        try:
            usuario = request.COOKIES["usuario"]
            turmas = calcularTurmas(db, usuario)
            return render(request, "turmas.html", {'usuario':usuario, '1º':turmas[0:4], "2º":turmas[4:8], "3º":turmas[8:12]})
        except:
            return erro(4)

def checar(request):
    global db

    if request.method == 'POST' and 'usuário' in request.POST:
        response = HttpResponseRedirect('/turmas/')
        usuario = request.POST["usuário"]

        senha = request.POST["senha"]

        db = d.conectar(usuario, senha)
        if not isinstance(db, str):
            response.set_cookie("usuario", usuario)
            si = secrets.token_hex(24)
            response.set_cookie("sessionid", si , max_age=(60**2)*2)

            d.atualizarUsuario(usuario, "sessãoAtual", si)
            return response
        else:
            e = db.replace("ERRO: ", "")
            db = None
            return erro(e)
            
    
    return render(request, 'login.html')