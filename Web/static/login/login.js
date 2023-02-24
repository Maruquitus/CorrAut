function ativacaoBotao(){

  if(!document.getElementById('senha').value.length || !document.getElementById('usuário').value.length  || senha.value.length < 8){
      document.getElementById("entrar").disabled = true;            
  }
  else{
      document.getElementById("entrar").disabled = false;

  }           
}

var func = function() {
  var senha = document.getElementById("senha");
  var usuário = document.getElementById("usuário");
  let style = window.getComputedStyle(usuário, "");
  let style2 = window.getComputedStyle(senha, "");
  if (style.backgroundColor !== "rgb(245, 245, 245)" && style2.backgroundColor !== "rgb(245, 245, 245)") {
      document.getElementById("entrar").disabled = false;
  }
}


window.onload = function() {
  setTimeout(func, 500);
}


function Função() {
    var x = document.getElementById("senha");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

function Entrar() {
  document.getElementById("load-div-container").style.display = "flex";
}