var função = function Função() {
  var quant = document.getElementById("quant").value;
  document.cookie = "questoes=" + quant.toString() + ";path=/cadastro/";
  location.reload();
  
}

var func = function Add() {
  document.getElementById("quant").addEventListener('onfocusout', função);
  document.getElementById("quant").addEventListener('change', função);
}

var destination;

var f2 = function back() {
  let url = window.location.href;
  window.location.href = url.replace("cadastro", destination);
}

window.onload = function() {
  setTimeout(func, 500);
}

function Red(d) {
  console.log("Executado");
  if (d == "turmas") {
    document.cookie = "voltou=1" + ";path=/";
  }
  else {
    document.cookie = "voltou=0" + ";path=/";
  }
  destination = d;
  
  document.getElementById("load-div-container").style.display = "flex";
  setTimeout(f2, 500);
}
