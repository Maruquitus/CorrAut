//Código da net pq fds
function alterarParametro(url, parametro, valor)
{
    if (valor == null) {
        valor = '';
    }
    var padrao = new RegExp('\\b('+parametro+'=).*?(&|#|$)');
    if (url.search(padrao)>=0) {
        return url.replace(padrao,'$1' + valor + '$2');
    }
    url = url.replace(/[?#]$/,'');
    return url + (url.indexOf('?')>0 ? '&' : '?') + parametro + '=' + valor;
}

function func2() {
  document.getElementById("load-div-container").style.display = "flex";
  setTimeout(f2, 1000);
}

var f2 = function F2() {
  var url = window.location.href.toString();
  url = alterarParametro(url.replace("cadastro", "turmas"), "turma", 0);
  url = url.replace("?turma=", "")
  window.location.href = url;
}


var função = function Função() {
  var quant = document.getElementById("quant").value;
  window.location.href = alterarParametro(window.location.href, "questoes", quant);
}

var func = function Add() {
  document.getElementById("quant").addEventListener('change', função);
}

window.onload = function() {
  setTimeout(func, 2000);
}

