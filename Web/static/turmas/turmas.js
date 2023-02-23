var turma;

var tr = function() {
    var url = window.location.href.toString();
    if (document.cookie) {
        document.cookie = "turma=" + turma.toString() + ";path=/";

        if (document.cookie.includes("voltou=1")) {
            document.cookie = "voltou=0" + ";path=/";
            window.location.href = url.replace("turmas", "cadastro");
        }
        else {
            window.location.href = url.replace("turmas", "dashboard");
        }
    }
    else {
        window.location.href = url.replace("turmas", "dashboard");
    }
}

function Red(t) {
    turma = t;
    
    document.getElementById("load-div-container").style.display = "flex";
    setTimeout(tr, 1000);
}
