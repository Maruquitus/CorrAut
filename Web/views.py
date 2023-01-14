from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def login(request):
    if request.method == 'GET':
        if "erro" in request.GET.keys():
            if request.GET["erro"]:
                return render(request, 'login.html', {"msgErro":"Usuário ou senha incorretos. Tente novamente."})
        
        
    return render(request, 'login.html')

def turmas(request):
    global db, usuario
    if usuario != None:
        return render(request, "turmas.html", {'usuario':usuario})
    else:
        return render(request, "turmas.html")

def checar(request):
    global db, usuario
    if request.method == 'POST' and 'usuário' in request.POST:
        usuario = request.POST["usuário"]
        senha = request.POST["senha"]

        import pymongo_get_database as d
        db = d.conectar(usuario, senha)
        if db != "ERRO":
            return HttpResponseRedirect('/turmas/')
        else:
            return HttpResponseRedirect('/login/?erro=True')
    
    return render(request, 'login.html')