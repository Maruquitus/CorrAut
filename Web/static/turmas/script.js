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

{
    var t;
}

var tr = function() {
    var url = window.location.href.toString();
    url = alterarParametro(url.replace("turmas", "cadastro"), "turma", t.toString());
    window.location.href = url;
}

function Red(turma) {
    t = turma;
    document.getElementById("load-div-container").style.display = "flex";
    setTimeout(tr, 1000);
}