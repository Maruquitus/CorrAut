function ativacaoBotao(){

  if(!document.getElementById('senha').value.length || !document.getElementById('usuário').value.length){
      document.getElementById("entrar").disabled = true;            
  }else{
      document.getElementById("entrar").disabled = false;

  }           
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